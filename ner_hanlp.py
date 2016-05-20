import sys
reload(sys)
sys.setdefaultencoding("utf8")
from jpype import *
startJVM(getDefaultJVMPath(), "-Djava.class.path=/home/cihang/HanLP/hanlp.jar:/home/cihang/HanLP")
ns = JClass("com.hankcs.hanlp.seg.NShort.NShortSegment")
ns_ner_seg = ns().enableAllNamedEntityRecognize(True)
text = open(sys.argv[1]).read()
term_list = ns_ner_seg.seg(text)
for i in xrange(0, len(term_list)):
    if str(term_list.get(i).nature) in ["ns", "nt", "ni", "nr"]:
        print term_list.get(i).word, term_list.get(i).nature
