# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/26
# ** Time: 10:00

import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import SVC, LinearSVC

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
# clf = SVC(gamma='auto',probability=True)
# clf = LinearSVC()
# # clf = CalibratedClassifierCV(clf)
# clf.fit(X, y)
# # SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
# print(clf.predict([[-0.8, -1]]))
# print(clf.decision_function([[-0.8, -1]]))

isotonic_svc = CalibratedClassifierCV(
    base_estimator=LinearSVC(),
    method='sigmoid',cv=2
) # isotonic calibration

isotonic_svc.fit(X, y)
print(isotonic_svc.predict([[-0.8, -1]]))
print(isotonic_svc.predict_proba([[-0.8, -1]]))

#
# from sklearn.linear_model import LogisticRegression
# import numpy as np
# x_train = np.array([[1, 2, 3],
#                     [1, 3, 4],
#                     [2, 1, 2],
#                     [4, 5, 6],
#                     [3, 5, 3],
#                     [1, 7, 2]])
#
# y_train = np.array([3, 3, 3, 2, 2, 2])
#
# x_test = np.array([[2, 2, 2],
#                    [3, 2, 6],
#                    [1, 7, 4]])
#
# clf = LogisticRegression()
# clf.fit(x_train, y_train)
#
# # 返回预测标签
# print(clf.predict(x_test))
#
# # 返回预测属于某标签的概率
# print(clf.predict_proba(x_test))
