import pickle
from pathlib import Path
from sklearn.linear_model import LinearRegression

from src.MatchAnalysis.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = LinearRegression(
            n_jobs=self.config.params_n_jobs
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        '''
        This function customize the model as you like, the code below is just an example as the linear regression doesn't need any customization
        '''

        return model
    
        """
        if freez_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten_in = tf.keas.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()
        
        return full_model
        """

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=None,
            freeze_all=None,
            freeze_till=None,
            learning_rate=None
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        
    @staticmethod
    def save_model(path: Path, model):
        with open(path, 'wb') as f:
            pickle.dump(model, f)

