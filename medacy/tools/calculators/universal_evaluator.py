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

        # Not entirely necessary, should be moved to unit testing
        assert isinstance(doc1, Annotations) # Replaced RecordTrack assertion with Annotation assertion
        assert isinstance(doc2, Annotations)
        assert mode in ("strict", "lenient")
        assert os.path.basename(doc1.source_text_path) == os.path.basename(doc2.source_text_path) # Replaced doc.basename to achieve the same result using Annotations
        
        self.scores = {"tp": 0, "fp": 0, "fn": 0, "tn": 0} # Removed relations from self.scores
        self.doc1 = doc1
        self.doc2 = doc2

        
        # From line ~79 in entity.py add conditional to check if annotations object

        gold = [a in doc1.annotations] # Confirm Annotations equlvalent of RecordTrack's tags
        prediction = [a in doc2.annotations]
        check = [a in doc2.annotations]
        # Removed key conditionals from variable assignment

        matches = []
        for p in prediction:
            for g in gold:
                if(g.equals(p, mode)): # TODO: Ensure (p, mode) works properly here
                    if g not in matched:
                        matched.append(g)
                    else:
                        if p in check:
                            check.remove(p)

        prediction = check # TODO: Ensure this shouldn't be changed

        # WIP
