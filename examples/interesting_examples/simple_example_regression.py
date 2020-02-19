import numpy
import sklearn.datasets
import sklearn.model_selection
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

from pytolemaic.pytrust import PyTrust
from pytolemaic.utils.dmd import DMD


def run():
    # Dataset: xtrain, ytrain, xtest, ytest
    data = sklearn.datasets.fetch_california_housing(return_X_y=False)

    x = data['data']
    y = data['target']
    feature_names = data['feature_names']

    train_inds, test_inds = sklearn.model_selection.train_test_split(
        numpy.arange(len(data['data'])), test_size=0.3)

    xtrain, ytrain = x[train_inds], y[train_inds]
    xtest, ytest = x[test_inds], y[test_inds]

    # Train estimator
    estimator = DecisionTreeRegressor()
    estimator.fit(xtrain, ytrain)

    # Initiating PyTrust
    pytrust = PyTrust(
        model=estimator,
        xtrain=xtrain, ytrain=ytrain,
        xtest=xtest, ytest=ytest,
        metric='mae')

    # Initiating PyTrust with feature names
    pytrust = PyTrust(
        model=estimator,
        xtrain=xtrain, ytrain=ytrain,
        xtest=xtest, ytest=ytest,
        columns_meta={DMD.FEATURE_NAMES: feature_names},
        metric='mae')
    scoring_report = pytrust.scoring_report()
    scoring_report.plot()

    sensitivity_report = pytrust.sensitivity_report()
    sensitivity_report.plot()

    quality_report = pytrust.quality_report()
    quality_report.plot()

    sample = xtest[0, :].reshape(1, -1)
    explainer = pytrust.create_lime_explainer(max_samples=64000)
    explainer.explain(sample=sample)

    uncertainty_model = pytrust.create_uncertainty_model(method='default')
    prediction = uncertainty_model.predict(sample)  # same as model.predict
    uncertainty = uncertainty_model.uncertainty(sample)  # uncertainty value


if __name__ == '__main__':
    run()
    plt.show()
