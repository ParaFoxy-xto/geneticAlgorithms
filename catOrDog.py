# image_classifier.py

import numpy as np

class ImageClassifier:
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def classify(self, new_image):
        # Distância euclidiana entre a nova imagem e todas as imagens conhecidas
        distances = np.sqrt(np.sum((self.features - new_image)**2, axis=1))

        # Encontra o índice da imagem mais próxima
        nearest_index = np.argmin(distances)
        return self.labels[nearest_index]

# Suponha que você tenha uma matriz "features" com as características das imagens conhecidas
# e um vetor "labels" com as categorias correspondentes (por exemplo, [0, 1, 0, 1, ...] onde 0 representa "cachorro" e 1 representa "gato").

# Exemplo:
features = np.array([
    [0.2, 0.1, 0.3],  # Características da imagem 1
    [0.8, 0.5, 0.7],  # Características da imagem 2
    # ...
])

labels = np.array([0, 1])  # 0 representa "cachorro", 1 representa "gato"

classifier = ImageClassifier(features, labels)

# Suponha que você tenha uma nova imagem com características "new_image":
new_image = np.array([0.25, 0.15, 0.35])

# Classifica a nova imagem:
result = classifier.classify(new_image)

if result == 0:
    print("A imagem é um cachorro.")
else:
    print("A imagem é um gato.")
