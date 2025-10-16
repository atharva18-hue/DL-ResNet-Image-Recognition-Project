import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
from torchvision import models
from tqdm import tqdm
import os

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--epochs', type=int, default=10)
    p.add_argument('--batch-size', type=int, default=128)
    p.add_argument('--lr', type=float, default=0.01)
    p.add_argument('--save-path', type=str, default='cifar_resnet18.pth')
    p.add_argument('--num-workers', type=int, default=2)
    return p.parse_args()

def train(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010)),
    ])
    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010)),
    ])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform_train)
    trainloader = DataLoader(trainset, batch_size=args.batch_size, shuffle=True, num_workers=args.num_workers)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform_test)
    testloader = DataLoader(testset, batch_size=256, shuffle=False, num_workers=args.num_workers)

    model = models.resnet18(pretrained=False, num_classes=10)
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=0.9, weight_decay=5e-4)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

    for epoch in range(args.epochs):
        model.train()
        running_loss = 0.0
        loop = tqdm(trainloader, desc=f'Epoch {epoch+1}/{args.epochs}')
        for inputs, targets in loop:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)
            loop.set_postfix(loss=loss.item())
        scheduler.step()
        epoch_loss = running_loss / len(trainloader.dataset)
        # simple evaluation
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for inputs, targets in testloader:
                inputs, targets = inputs.to(device), targets.to(device)
                outputs = model(inputs)
                _, predicted = outputs.max(1)
                total += targets.size(0)
                correct += predicted.eq(targets).sum().item()
        acc = 100. * correct / total
        print(f'Epoch {epoch+1} finished. Loss: {epoch_loss:.4f}  Test Acc: {acc:.2f}%')
        # save checkpoint
        torch.save({'epoch': epoch+1, 'model_state_dict': model.state_dict(), 'acc': acc}, args.save_path)
    print('Training finished. Last checkpoint saved to', args.save_path)

if __name__ == '__main__':
    args = get_args()
    os.makedirs(os.path.dirname(args.save_path) or '.', exist_ok=True)
    train(args)
