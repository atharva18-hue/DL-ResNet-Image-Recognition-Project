const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const predictionText = document.getElementById('predictionText');
const infoDiv = document.getElementById('info');
const tryAnotherBtn = document.getElementById('tryAnotherBtn');

const classInfo = {
  "cat": [
    "1. Cats are agile, graceful, and independent animals.",
    "2. They communicate using meows, purrs, and body language.",
    "3. Cats can see in near darkness, making them excellent hunters.",
    "4. Domesticated for over 9,000 years.",
    "5. Have retractable claws for silent movement.",
    "6. Cats spend up to 16 hours a day sleeping.",
    "7. Their whiskers help them sense their surroundings.",
    "8. Extremely curious and territorial by nature.",
    "9. Known for their grooming habits and cleanliness.",
    "10. Cats have excellent balance and flexibility."
  ],
  "dog": [
    "1. Dogs are loyal, social, and intelligent companions.",
    "2. Domesticated from wolves thousands of years ago.",
    "3. Excellent sense of smell — 40x stronger than humans.",
    "4. Used for rescue, therapy, and military service.",
    "5. Communicate through barking, tail wagging, and posture.",
    "6. Come in more than 340 recognized breeds.",
    "7. Recognize human emotions and facial expressions.",
    "8. Lifespan varies from 10 to 15 years on average.",
    "9. Known as man’s best friend for their faithfulness.",
    "10. Require regular exercise and affection to thrive."
  ],
  "airplane": [
    "1. Airplanes are modern marvels of aerodynamics.",
    "2. Use engines to generate thrust and wings for lift.",
    "3. Can travel at speeds exceeding 900 km/h.",
    "4. Play a vital role in connecting the world.",
    "5. Equipped with advanced navigation systems.",
    "6. Made of lightweight composite materials.",
    "7. Require strict safety and maintenance checks.",
    "8. Pilots control via cockpit instruments and avionics.",
    "9. Can fly up to 35,000 feet above sea level.",
    "10. Revolutionized transportation and global trade."
  ],
  "frog": [
    "1. Frogs are amphibians that live both on land and in water.",
    "2. Known for their jumping ability and croaking sound.",
    "3. They breathe through their skin and lungs.",
    "4. Play a crucial role in controlling insect populations.",
    "5. Found on every continent except Antarctica.",
    "6. Their sticky tongue helps catch prey quickly.",
    "7. Go through metamorphosis — from tadpole to adult frog.",
    "8. Sensitive to environmental changes and pollution.",
    "9. Some frogs have bright colors to warn predators.",
    "10. Serve as important indicators of ecosystem health."
  ],
  "house": [
    "1. A house provides shelter and safety to its occupants.",
    "2. Built using materials like brick, wood, or concrete.",
    "3. Reflects the lifestyle and culture of the people living in it.",
    "4. Divided into functional spaces such as rooms and hallways.",
    "5. Modern houses include smart home technologies.",
    "6. Plays a key role in family bonding and comfort.",
    "7. Architectural designs vary worldwide based on climate.",
    "8. Energy-efficient homes reduce environmental impact.",
    "9. Can be personalized with furniture and décor.",
    "10. Symbolizes stability, belonging, and personal identity."
  ]
};

// 🧠 Handle image upload and prediction
imageInput.addEventListener('change', async (event) => {
  const selectedFile = event.target.files[0];
  if (!selectedFile) return;

  preview.src = URL.createObjectURL(selectedFile);
  preview.style.display = 'block';
  predictionText.textContent = "Analyzing image...";
  infoDiv.innerHTML = "";

  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const response = await fetch('/predict', { method: 'POST', body: formData });
    const data = await response.json();

    if (data.prediction) {
      const predictedClass = data.prediction.toLowerCase();
      predictionText.textContent = `Predicted Class: ${predictedClass.toUpperCase()}`;
      const lines = classInfo[predictedClass] || ["No information available for this image."];
      infoDiv.innerHTML = lines.map(line => `<p>${line}</p>`).join('');
    } else {
      predictionText.textContent = "Prediction failed!";
    }
  } catch (err) {
    console.error(err);
    predictionText.textContent = "Error occurred during prediction!";
  }
});

// 🔁 Reset interface
tryAnotherBtn.addEventListener('click', () => {
  imageInput.value = '';
  preview.style.display = 'none';
  predictionText.textContent = "Upload an image to see the prediction...";
  infoDiv.innerHTML = '';
});
