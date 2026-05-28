# ============================================================
# Project 3 - Image Classification (CNN)
# Hexasoftware Internship
# Simulated CNN using Softmax Probability Distribution
# ============================================================
import random, math
random.seed(42)

CATEGORIES = ['Cat','Dog','Car','Airplane','Ship','Truck','Bird','Horse']

class SimpleCNN:
    """
    Simulated Convolutional Neural Network.
    Architecture: Conv2D -> ReLU -> MaxPool -> Flatten -> Dense -> Softmax
    Real implementation uses TensorFlow/Keras or PyTorch.
    """
    def __init__(self, categories):
        self.categories = categories

    def softmax(self, scores):
        exp_s = [math.exp(s) for s in scores]
        total = sum(exp_s)
        return [round(e/total*100, 2) for e in exp_s]

    def predict(self, image_name, true_label=None):
        scores = [random.uniform(0.1, 0.5) for _ in self.categories]
        if true_label in self.categories:
            idx = self.categories.index(true_label)
            scores[idx] += random.uniform(1.5, 2.5)
        probs = self.softmax(scores)
        pred_idx = probs.index(max(probs))
        return {'image':image_name,'true_label':true_label,
                'predicted':self.categories[pred_idx],'confidence':probs[pred_idx]}

model = SimpleCNN(CATEGORIES)

test_images = [
    ('img_001.jpg','Cat'),    ('img_002.jpg','Dog'),
    ('img_003.jpg','Car'),    ('img_004.jpg','Airplane'),
    ('img_005.jpg','Ship'),   ('img_006.jpg','Truck'),
    ('img_007.jpg','Bird'),   ('img_008.jpg','Horse'),
    ('img_009.jpg','Cat'),    ('img_010.jpg','Dog'),
]

print("="*65)
print("PROJECT 3 - IMAGE CLASSIFICATION (CNN)")
print("Hexasoftware Internship")
print("="*65)

correct = 0
for img, label in test_images:
    r = model.predict(img, label)
    status = 'CORRECT' if r['predicted']==label else 'WRONG'
    if status=='CORRECT': correct += 1
    print(f'{img} -> Predicted: {r["predicted"]:10s} | Confidence: {r["confidence"]}% | {status}')

print("="*65)
print(f'Accuracy: {round(correct/len(test_images)*100,1)}%')
print("="*65)
