import json
import abc

class ModelInterface:
    __metaclass__  = abc.ABCMeta
    def __init__(self, model_name, retrain_counter, model_type):
        self.model_name = model_name
        self.model_type = model_type
        self.trained = False
        self.available_data = 0
        self.used_training_data = 0
        self.retrain_counter = retrain_counter

    def avail_data_incr(self):
        self.available_data += 1

    def set_data_format(self, col_names):
        self.col_names = col_names

    def update_mdl_state(self):
        self.used_training_data = self.available_data
        self.trained = True

    @abc.abstractmethod
    def get_parameters(self):
        """This method needs to be implemented"""

    @abc.abstractmethod
    def train(self, train_data):
        """This method needs to be implemented"""

    @abc.abstractmethod
    def score(self, score_data):
        """This method needs to be implemented"""

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __str__(self):
        obj_dict = self.__dict__
        if self.trained:
            obj_dict['parameters'] = self.get_parameters()
        return str(obj_dict)


def train_wrapper(func):
    def wrapper(self, data):
        # pre-process data
        dict_data = [json.loads(el) for el in data]
        col_names = dict_data[0].keys()

        # # run some update functions on the object
        # if not self.trained:
        #     self.set_data_format(col_names)
        # else:
        #     if self.col_names != col_names:
        #         raise InputError('Data format is not the same as used before.')

        # run the actual training function
        val = func(self, dict_data, col_names)

        # update the model state
        self.update_mdl_state()

        return val

    return wrapper


def createModel(model_type, model_name, retrain_counter):
    try:
        import StandardModels
        return getattr(StandardModels, model_type)(model_name, retrain_counter)
    except:
        try:
            import CustomModels
            return getattr(CustomModels, model_type)(model_name, retrain_counter)
        except:
            return None
