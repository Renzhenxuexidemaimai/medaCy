from medacy.data import Dataset
from medacy.ner.model import Model
from medacy.ner.pipelines import LstmSystematicReviewPipeline
import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

n2c2_dataset = Dataset(data_directory="/home/conteam/Data/N2C2_Data")

pipeline = LstmSystematicReviewPipeline(entities=['ADE', 'Dosage', 'Drug'],
                                        word_embeddings='/home/conteam/Data/mimic3_d200.bin', cuda_device=0)
model = Model(pipeline)

model.cross_validate(training_dataset=n2c2_dataset)




