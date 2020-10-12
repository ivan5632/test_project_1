import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wikipedia
from sklearn.feature_extraction.text import CountVectorizer


def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def cosine_similarity(x, y):
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

def l1_normalize(v):
    norm = np.sum(v)
    return v / norm

def l2_normalize(v):
    norm = np.sqrt(np.sum(np.square(v)))
    return v / norm


# x = list(range(-4,4,1))
# y = [0.2,0.5,0.3,1.2,-0.8,-1.6,-1.5,1.4]
# print(x,y)
# plt.plot(x,y)
# plt.show()

# X = np.array([[6.6, 6.2, 1],
#               [9.7, 9.9, 2],
#               [8.0, 8.3, 2],
#               [6.3, 5.4, 1],
#               [1.3, 2.7, 0],
#               [2.3, 3.1, 0],
#               [6.6, 6.0, 1],
#               [6.5, 6.4, 1],
#               [6.3, 5.8, 1],
#               [9.5, 9.9, 2],
#               [8.9, 8.9, 2],
#               [8.7, 9.5, 2],
#               [2.5, 3.8, 0],
#               [2.0, 3.1, 0],
#               [1.3, 1.3, 0]])
#
# df = pd.DataFrame(X, columns=['weight', 'length', 'label'])
# print(df)
#
# ax = df[df['label'] == 0].plot.scatter(x='weight', y='length', c='blue', label='young')
# ax = df[df['label'] == 1].plot.scatter(x='weight', y='length', c='orange', label='mid', ax=ax)
# ax = df[df['label'] == 2].plot.scatter(x='weight', y='length', c='red', label='adult', ax=ax)
#
# df2 = pd.DataFrame([df.iloc[0], df.iloc[1], df.iloc[4]], columns=['weight', 'length', 'label'])
# df3 = pd.DataFrame([df.iloc[14]], columns=['weight', 'length', 'label'])
#
# ax = df2[df2['label'] == 0].plot.scatter(x='weight', y='length', c='blue', label='young')
# ax = df2[df2['label'] == 1].plot.scatter(x='weight', y='length', c='orange', label='mid', ax=ax)
# ax = df2[df2['label'] == 2].plot.scatter(x='weight', y='length', c='red', label='adult', ax=ax)
# ax = df3.plot.scatter(x='weight', y='length', c='gray', label='?', ax=ax)
#
# x0 = X[0][:-1]
# x1 = X[1][:-1]
# x4 = X[4][:-1]
# x14 = X[14][:-1]
# print(" x0:", x0, "\n x1:", x1, "\n x4:", x4, "\nx14:", x14)
#
# print("x14 and x0:", euclidean_distance(x14, x0), "\n",
#       "x14 and x1:", euclidean_distance(x14, x1), "\n",
#       "x14 and x4:", euclidean_distance(x14, x4))
#
# print(" x14 and x0:", cosine_similarity(x14, x0), "\n",
#       "x14 and x1:", cosine_similarity(x14, x1), "\n",
#       "x14 and x4:", cosine_similarity(x14, x4))
#
# print("vectors \t", x0, x1, "\n"
#       "euclidean \t", euclidean_distance(x0, x1), "\n"
#       "cosine \t\t", cosine_similarity(x0, x1))
#
# x0_n = l1_normalize(x0)
# x1_n = l1_normalize(x1)
# print(x0_n, x1_n)
#
# print("vectors \t", x0_n, x1_n, "\n"
#       "euclidean \t", euclidean_distance(x0_n, x1_n), "\n"
#       "cosine \t\t", cosine_similarity(x0_n, x1_n))
#
# print("vectors \t", x0, x4, "\n"
#       "euclidean \t", euclidean_distance(x0, x4), "\n"
#       "cosine \t\t", cosine_similarity(x0, x4))
#
# x4_n = l1_normalize(x4)
# print("vectors \t", x0_n, x4_n, "\n"
#       "euclidean \t", euclidean_distance(x0_n, x4_n), "\n"
#       "cosine \t\t", cosine_similarity(x0_n, x4_n))
#

q1 = wikipedia.page('Machine Learning')
q2 = wikipedia.page('Artificial Intelligence')
q3 = wikipedia.page('Soccer')
q4 = wikipedia.page('Tennis')
cv = CountVectorizer()
X = np.array(cv.fit_transform([q1.content, q2.content, q3.content, q4.content]).todense())
# # print("ML \t", len(q1.content.split()), "\n"
# #       "AI \t", len(q2.content.split()), "\n"
# #       "soccer \t", len(q3.content.split()), "\n"
# #       "tennis \t", len(q4.content.split()))
#
# print("ML - AI \t", euclidean_distance(X[0], X[1]), "\n"
#       "ML - soccer \t", euclidean_distance(X[0], X[2]), "\n"
#       "ML - tennis \t", euclidean_distance(X[0], X[3]))
#
# print("ML - AI \t", cosine_similarity(X[0], X[1]), "\n"
#       "ML - soccer \t", cosine_similarity(X[0], X[2]), "\n"
#       "ML - tennis \t", cosine_similarity(X[0], X[3]))

ml_tweet = "New research release: overcoming many of Reinforcement Learning's limitations with Evolution Strategies."
x = np.array(cv.transform([ml_tweet]).todense())
print(x)

print("tweet - ML \t", euclidean_distance(x[0], X[0]), "\n"
      "tweet - AI \t", euclidean_distance(x[0], X[1]), "\n"
      "tweet - soccer \t", euclidean_distance(x[0], X[2]), "\n"
      "tweet - tennis \t", euclidean_distance(x[0], X[3]))

print("tweet - ML \t", cosine_similarity(x, X[0]), "\n"
      "tweet - AI \t", cosine_similarity(x, X[1]), "\n"
      "tweet - soccer \t", cosine_similarity(x, X[2]), "\n"
      "tweet - tennis \t", cosine_similarity(x, X[3]))

# plt.show()