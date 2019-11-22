import argparse
import glob
import os
from collections import defaultdict
from xml.etree import cElementTree
from medacy.data.annotations import Annotations
from medacy.data.dataset import Dataset
from medacy.tools.entity import Entity


# Setup
parser = argparse.ArgumentParser(description="Evaluation script")
parser.add_argument("folder1", help="Path to first data directory (gold)")
parser.add_argument("folder2", help="Path to second data directory (prediction)")
args = parser.parge_args()

gold_dataset = Dataset(args.folder1)
prediction_dataset = Dataset(args.folder2)
global_tags = tuple(gold_dataset.get_labels() & prediction_dataset.get_labels())


# SingleEvaluator
class SingleEvaluator(object):

    def __init__(self, doc1, doc2, mode="strict", key=None, verbose=False):

        assert isinstance(doc1, Annotations) # Replaced RecordTrack assertion with Annotation assertion
        assert isinstance(doc2, Annotations)
        assert mode in ("strict", "lenient")
        assert os.path.basename(doc1.source_text_path) == os.path.basename(doc2.source_text_path) # Replaced doc.basename to achieve the same result using Annotations
        
        self.scores = {"tags": {"tp": 0, "fp": 0, "fn": 0, "tn": 0}} # Removed relations from self.scores
        self.doc1 = doc1
        self.doc2 = doc2

        # Removed key conditionals and doc.relations.values() assignments

        # WIP
