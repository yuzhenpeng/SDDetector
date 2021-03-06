#!/usr/bin/env python

import sqlite3
import unittest

from SDDetector.Entities.Alignment import Alignment
from SDDetector.Entities.Region import Region
from SDDetector.Parser.Blast.BlastXMLParserExpat import BlastXMLParserExpat

class TestBlastXMLParserExpat(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getAllAlignments(self):
        """Test getAllAlignments method"""

        iBlastXMLParser = BlastXMLParserExpat("test-data/blast.xml")
        lAlignments = [Alignment('seq1','seq1',1,167,1,167,167,167,1,1,id=1),
                       Alignment('seq1','seq2',1,164,237,400,164,164,1,-1,id=2),
                       Alignment('seq1','seq2',50,113,54,118,66,63,1,1,id=3),
                       Alignment('seq2','seq2',1,400,1,400,400,400,1,1,id=4),
                       Alignment('seq2','seq2',288,351,54,118,66,63,1,-1,id=5),
                       Alignment('seq2','seq2',54,118,288,351,66,63,1,-1,id=6),
                       Alignment('seq2','seq1',237,400,1,164,164,164,1,-1,id=7),
                       Alignment('seq2','seq1',54,118,50,113,66,63,1,1,id=8)]

        self.assertEqual(iBlastXMLParser.getAllAlignments()[4],lAlignments[4])

    def test_getAlignmentsFromTupleOfRegions(self):
        """Test getAlignmentsFromTupleOfRegions method"""

        iBlastXMLParser = BlastXMLParserExpat("test-data/blast.xml")
        lRegions = [(Region('seq1',1,167,1),Region('seq1',1,167,1)),
                    (Region('seq1',1,164,-1),Region('seq2',237,400,1)),
                    (Region('seq2',288,351,-1),Region('seq2',54,118,1))]
        lAlignments = [('ATGATGCTCGTAGAGAGCGCTCGCCGTAGAGGATAGTGCGGCTCGATGATGAAGTCGCTGTTTTGGCTGTAGGATAGCGGTGGTCTCGATTAGCCTAGAGGATAATTATAGCTCGTCAAAATTTTATATGTCGCCTAGATAGTCTCCGATTAGATCGGCTAGGATCG','ATGATGCTCGTAGAGAGCGCTCGCCGTAGAGGATAGTGCGGCTCGATGATGAAGTCGCTGTTTTGGCTGTAGGATAGCGGTGGTCTCGATTAGCCTAGAGGATAATTATAGCTCGTCAAAATTTTATATGTCGCCTAGATAGTCTCCGATTAGATCGGCTAGGATCG'),
                       ('TCCTAGCCGATCTAATCGGAGACTATCTAGGCGACATATAAAATTTTGACGAGCTATAATTATCCTCTAGGCTAATCGAGACCACCGCTATCCTACAGCCAAAACAGCGACTTCATCATCGAGCCGCACTATCCTCTACGGCGAGCGCTCTCTACGAGCATCAT','TCCTAGCCGATCTAATCGGAGACTATCTAGGCGACATATAAAATTTTGACGAGCTATAATTATCCTCTAGGCTAATCGAGACCACCGCTATCCTACAGCCAAAACAGCGACTTCATCATCGAGCCGCACTATCCTCTACGGCGAGCGCTCTCTACGAGCATCAT'),
                       ('TGA-AGTCGCT-GTTTTGGCTGTAGGATAGCGGTGGTCTCGATTAGCCTAGAGGATAATTATAGCT','TGATAGT-GCTGGTTTTGGCTGTAGGATAGCGGTGGTCTCGATTAGCCTAGAGGATAATTATAGCT')]

        self.assertEqual(iBlastXMLParser.getAlignmentsFromTupleOfRegions(lRegions),lAlignments)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBlastXMLParserExpat)
    unittest.TextTestRunner(verbosity=2).run(suite)

