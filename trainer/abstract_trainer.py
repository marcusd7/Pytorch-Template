
class AbstractTrainer(object):
    r"""Trainer Class is used to manage the training and evaluation processes
    AbstractTrainer is an abstract class in which the fit() and evaluate() method should be implemented according
    to different training and evaluation strategies.
    """

    def __init__(self, config, model):
        self.config = config
        self.model = model

    def optimizer(self):
        r"""Optimizer used to optimize the parameters

        """
        raise NotImplementedError

    def LossFunc(self):
        r"""Loss Objective Function

        """
        raise NotImplementedError

    def fit(self, train_data):
        r"""Train the model based on the train data.
        e.g 
        for (data, label) in xxxdataloader:
            pred = model(data)
            optimizer.zero_grad()
            loss = LossFunc(pred, label)
            loss.backward()
            optimizer.step()
        """
        raise NotImplementedError('Method [next] should be implemented.')

    def evaluate(self, eval_data):
        r"""Evaluate the model based on the eval data.

        """

        raise NotImplementedError('Method [next] should be implemented.')