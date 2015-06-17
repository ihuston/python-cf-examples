from ModelFactory import ModelInterface, train_wrapper
from sklearn import linear_model

class LinearRegression(ModelInterface):
    def __init__(self, name, rt_counter):
        ModelInterface.__init__(self, name, rt_counter, 'LinearRegression')

    @train_wrapper
    def train(self, data, col_names):
        col_names.remove('label')

        x = [[el[key] for key in col_names] for el in data]
        y = [el['label'] for el in data]

        self.mdl = linear_model.LinearRegression()
        self.mdl.fit(x, y, 1)

        return self.get_parameters()

    def score(self, data):
        return self.mdl.predict(data)

    def get_parameters(self):
        coefficients = self.mdl.coef_.tolist()
        coefficients.append(self.mdl.intercept_)

        col_names = self.col_names[:]
        col_names.remove('label')
        col_names.append('constant')

        return dict(zip(col_names, coefficients))
