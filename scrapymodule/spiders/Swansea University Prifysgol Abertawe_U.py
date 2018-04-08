# -*- coding: utf-8 -*-
import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.getItem import get_item1
from scrapymodule.getTuition_fee import getTuition_fee
from scrapymodule.items import SchoolItem2
import requests
from lxml import etree
from scrapymodule.getIELTS import get_ielts, get_toefl

class SwanseaBenShoolSpider(scrapy.Spider):
    name = "swanseaBen"
    # allowed_domains = ['baidu.com']
    start_urls = ["http://www.swansea.ac.uk/undergraduate/courses/som/bscaccounting/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscaccountingandfinance/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscaccfinance-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscaccounting-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscaccounting-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscaccfinance-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsadultnursingcarmarthen/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsadultnursingswansea/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/meng-aerospace-engineering-h403/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/beng-aerospace-engineering-h400/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/meng-aerospace-engineering-h406/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/beng-aerospace-engineering-abroad-h401u/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/meng-aerospace-engineering-industry-h404/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/beng-aerospace-engineering-industry-h402/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/aerospace-engineering/beng-aerospace-engineering-foundation-year-h405/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-americanstudies-t701/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-english-tq73/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-amsgeog-lt77/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-amsgeog-tl77/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-history-vt17/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-history-tv71/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-politics-lt27/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-politics-tl72/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-americanstudies-t700/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ancienthistory-v112/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ancienthistory-english-vq13/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-anchistfrench-vr11/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ahistger-vr12/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ancienthistory-greek-vq17/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ancienthistory-history-v110/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ancienthisthist-v190/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ahistlatin-vq16/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ahistpol-vl12/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ahistspa-vr14/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ancient-and-medieval-history/ba-ancientmedievalhistory-v116/",
"http://www.swansea.ac.uk/undergraduate/courses/som/fdscapplbusman/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-applied-mathematics-g120/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscappliedmedicalsciences/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/appliedmedicalscienceswithafoundationyear/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/certificateofhighereducationinbasicaudiologicalpractice/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mscibiochemistry/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscbiochemistry/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscbiochemistryandgenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mscibiochemistryandgenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-biological-science-with-deferred-choice-c100/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-biological-sciences-with-a-year-abroad-with-deferred-choice-c105/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-biology-c104/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-biology-with-a-year-abroad-c106/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-biology-with-a-year-in-industry-c152/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-biology-with-foundation-year-c101/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/graduate_certificate_blood_component_transfusion/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llbbusinesslaw/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusman-busanalytics/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-busanalytics-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-busanalytics-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagemententrepreneurship/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-ent-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-ent-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementfinance/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-finance-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-finance-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementhumanresourcesmanagement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-hrm-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-hrm-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementmanagementconsulting/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-manconsulting-yearabroad",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-manconsulting-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementmarketing/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-marketing-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-marketing-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-osm-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementoperationsandsupplymanagement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-osm-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagementtourism/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusinessmanagementtourism-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusinessmanagementtourism-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscbusinessmanagemente-business/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-ebusiness-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-ebusiness-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscbusman-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscbusman-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/meng-chemical-engineering-h801/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/beng-chemical-engineering-h831/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/meng-chemical-engineering-industry-h890/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/meng-chemical-engineering-h802d/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/beng-chemical-engineering-h800d/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/beng-chemical-engineering-foundation-year-h835/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/chemical-engineering/beng-chemical-engineering-industry-h832/",
"http://www.swansea.ac.uk/undergraduate/courses/science/chemistry/mchem-chemistry-f123/",
"http://www.swansea.ac.uk/undergraduate/courses/science/chemistry/bsc-chemistry-f100/",
"http://www.swansea.ac.uk/undergraduate/courses/science/chemistry/bsc-chemistry-with-a-year-abroad-f106/",
"http://www.swansea.ac.uk/undergraduate/courses/science/chemistry/bsc-chemistry-with-a-year-in-industry-f101/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/beng-civil-engineering-h200/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/meng-civil-engineering-h201/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/meng-civil-engineering-industry-h204/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/beng-civil-engineering-h206d/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/meng-civil-engineering-h207d/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/beng-civil-engineering-foundation-year-h205/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/civil-engineering/beng-civil-engineering-industry-h202/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-classciv-q820/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-classciv-englishlit-qq83/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ccivfrench-qr81/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ccivger-qr82/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-classciv-greek-qq78/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/qq86/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-ccivmedstu-qvv1/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-classics-q800/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/bsc_community_health_studies_community_mental_health_nursing/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-computer-science-g400/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/msci-computer-science-g4g4/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/bsc-computer-science-with-a-year-abroad-g40c/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/msci-computer-science-with-a-year-abroad-g4g2/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/bsc-computer-science-with-a-year-in-industry-g40a/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/msci-computer-science-with-a-year-in-industry-g847/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-computer-science-with-foundation-year-g401/",
"http://www.swansea.ac.uk/undergraduate/courses/science/meng-computing-g403/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/meng-computing-with-a-year-abroad-g40d/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/meng-computing-with-a-year-in-industry-g40b/",
"http://www.swansea.ac.uk/undergraduate/courses/law/bsccriminologycriminaljustice/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonscriminologyandpsychology/",
"http://www.swansea.ac.uk/undergraduate/courses/law/bsccriminologysocialpolicy/",
"http://www.swansea.ac.uk/cy/israddedig/cyrsiau/celfyddydau-a-r-dyniaethau/cyfryngau-cyfathrebu/bacyfryngauachysylltiadaucyhoeddus/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/bacyfryngauachysylltiadaucyhoeddusgydablwyddynmewndiwydiant4blynedd/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/cymraeg-welsh/ba-cymraegcyfryngaucysylltiadaucyhoeddus-qp53/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-germanandwelsh-q5r2/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchandwelsh-q5r1/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/spanish/ba-spanishandwelsh-q5r4/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bsceconomics/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscecon-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bsceconomicsbusiness/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bsceconandbus-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bsceconandbus-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bsceconomicsfinance/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bsceconandfin-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bsceconandfin-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscecon-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/ba-hons-education/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/bsc-hons-education-and-computing/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/bsc-hons-education-and-mathematics/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/bsc-hons-education-and-psychology/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/ba-hons-education-and-welsh/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-egyptology-v410/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-egyahist-vv41/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/classics-ancient-history-and-egyptology/ba-egyahist-vq48/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/electrical-engineering/beng-electronic-and-electrical-engineering-h602/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/electrical-engineering/meng-electronic-and-electrical-engineering-h606/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/electrical-engineering/meng-electronic-and-electrical-eng-year-out-h600/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/electrical-engineering/beng-electronic-electrical-eng-year-out-h603/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/electrical-engineering/beng-electrical-engineering-foundation-year-h605/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/engineering-foundation-year/beng-engineering-with-a-foundation-year-h101/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-chinesetranslationandinterpreting/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englishlanguage-q310/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englishlanguage-q311/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englangenglit-qq31/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-english-language-qrj3/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/ba-mediaenglish-pq91/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-mediaenglish-pq00/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englang-spanish-qrj4/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-tesol-qx33/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishliterature-q300/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishliterature-qh20/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-english-qt37/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englangenglit-qq3d/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitfrench-qr31/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitgerman-qr32/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englithis-qv31/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englithis-qv3c/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-english-literature-qr33/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitmedstu-qvh1/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitspanish-qr34/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishliteratureandwelsh-qq3n/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishliteratureandwelsh-qqh5/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-english-creative-writing-q3w9/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishgender-q3l3/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englishgender-qhl3/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsenhancedparamedicpractice/",
"http://www.swansea.ac.uk/humanandhealthsciences/work-based-learning/certhe_enhanced_practice/",
"http://www.swansea.ac.uk/humanandhealthsciences/work-based-learning/bsc_graddip_enhanced_professional_practice/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscfinance/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscfinance-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscfinance-yearworkplacement/",
"http://www.swansea.ac.uk/itwales/foundation-degree/",
"http://www.swansea.ac.uk/itwales/foundation-degree/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-french-r101/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englangfrench-qrj1/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchger-rr12/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchhist-rv11/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-french-rr13/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchpol-lr21/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchspa-rr14/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchandwelsh-qr51/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/bsc-general-practice-nursing/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscgenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mscigenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-geography-f800/",
"http://www.swansea.ac.uk/undergraduate/courses/science/ba-geography-l700/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/ba-geography-with-a-year-abroad-l701/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/ba-geography-with-a-year-in-industry-f554/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/bsc-geography-with-a-year-in-industry-f273/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-geography-and-geo-informatics-f830/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-geography-with-foundation-year-fl87/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/bsc-geography-with-a-year-abroad-f8r9/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-german-r220/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-englanggerman-qrj2/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-gerhist-rv21/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-german-rr23/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-gerpol-lr22/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-germanpanish-rr24/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-germanandwelsh-qr52/",
"http://www.swansea.ac.uk/postgraduate/taught/law/graduatediplomainlaw/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/bsc_graddip_gradcert_health_care_practice_bsc_graddip_gradcert_nursing_practice/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/certificateinhealthcarestudiesforhealthcaresupportworkers/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthandsocialcare/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceaudiology/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencecardiacphysiology/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceneurophysiology/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencenuclearmedicine/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceradiationphysics/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceradiotherapyphysics/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencerespiratoryandsleepphysiology/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-history-v100/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-history-v101/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-history-rv31/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-histmedieval-v130/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-histmedieval-v191/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-histpol-lv21/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-polhist-vl1f/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-social-history-social-policy/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-histspanish-rv41/",
"http://www.swansea.ac.uk/undergraduate/courses/science/ba-human-geography-l720/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/ba-human-geography-with-a-year-in-industry-l987/",
"http://www.swansea.ac.uk/undergraduate/courses/law/mlawhumanrights/",
"http://www.swansea.ac.uk/dace/students/aboutourprogrammes/bahumanitieshistoryandenglishpart-timedegrees/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-ir-l254/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/american-studies/ba-ams-ir-lt2r/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-modhistory-ir-lv2c/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-irfrench-l2rd/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-irgerman-%20l2r2/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-irspanish-l2r4/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/ba-italian/ba-italian-spanish-rr34/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llbsinglehonourslaw/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawcrimecriminaljustice/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llbseniorstatus/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandamericanstudies/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandamericanstudieswithanintercalaryyear/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandcriminology/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandfrench/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandgerman/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandhistory/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawanditalian/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandmedia/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandpolitics/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandspanish/",
"http://www.swansea.ac.uk/undergraduate/courses/law/llblawandwelsh/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-marine-biology-c160/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-marine-biology-with-a-year-abroad-c107/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-marine-biology-with-a-year-in-industry-c424/",
"http://www.swansea.ac.uk/undergraduate/courses/som/bscmarketing/",
"http://www.swansea.ac.uk/undergraduate/courses/som/study-abroad/bscmarketing-yearabroad/",
"http://www.swansea.ac.uk/undergraduate/courses/som/4yr/bscmarketing-yearworkplacement/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/meng-materials-science-engineering-j504/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/beng-materials-science-engineering-j500/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/meng-materials-science-engineering-industry-j503/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/beng-materials-science-engineering-industry-j502/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/beng-materials-science-engineering-abroad-j510/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/beng-materials-engineering-foundation-year-j505/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/materials-engineering/meng-materials-science-engineering-j506/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/maternity-care/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-mathematics-g100/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mmath-mathematics-g103/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/mmath-mathematics-with-a-year-abroad-g105/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/bsc-mathematics-with-a-year-abroad-g104/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/bsc-mathematics-with-a-year-in-industry-g327/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/bsc-mathematics-and-sport-and-exercise-science-gc16/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-mathematics-for-finance-g190/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/bsc-mathematics-for-finance-with-a-year-abroad-g191/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mathematics/bsc-mathematics-for-finance-with-a-year-in-industry-g956/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-mathematics-with-foundation-year-g101/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/beng-mechanical-engineering-h300/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/meng-mechanical-engineering-h304/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/meng-mechanical-engineering-industry-h306/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/beng-mechanical-engineering-foundation-year-h307/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/beng-mechanical-engineering-h308/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/meng-mechanical-engineering-h309/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/mechanical-engineering/beng-mechanical-industry-h305/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/ba-media-p300/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/ba-media-p407/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitmedia-qp33/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/french/ba-frenchmedia-pr31/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/german/ba-germedia-pr32/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/ba-mediaspan-pr34/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mscimedicalbiochemistry/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscmedicalbiochemistry/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/beng-medical-engineering-hb18/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/meng-medical-engineering-hb1v/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/meng-medical-engineering-hb02/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/beng-medical-engineering-hb01/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/beng-medical-engineering-foundation-year-hbc9/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/meng-medical-engineering-year-in-industry-hb1w/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/medical-engineering/beng-medical-engineering-year-in-industry-hb19/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mscimedicalgenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/bscmedicalgenetics/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/pharmacology/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/mbbchgraduateentrymedicine/",
"http://www.swan.ac.uk/undergraduate/courses/human-and-health-sciences/bmidhonsmidwifery/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bmidhonsshortpre-registrationmidwifery/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/bamodernlanguages/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/modern-languages-translation-and-interpreting/ba-modenlangtrans-q910/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonschildnursing/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsmentalhealthnursing/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/bsc_graddip_gradcert_health_care_practice_bsc_graddip_gradcert_nursing_practice/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/mostosteopathy/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/dipheparamedicscience/",
"http://www.swan.ac.uk/undergraduate/courses/human-and-health-sciences/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-ppe-l0v0/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-physical-earth-science-ff86/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/bsc-physical-earth-science-with-a-year-in-industry-f769/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-physical-geography-f840/",
"http://www.swansea.ac.uk/undergraduate/courses/science/geography/bsc-physical-geography-with-a-year-in-industry-f931/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mphys-physics-f303/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-physics-f300/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mphys-physics-with-a-year-abroad-f304/",
"http://www.swansea.ac.uk/undergraduate/courses/science/physics/bsc-physics-with-a-year-in-industry-f478/",
"http://www.swansea.ac.uk/undergraduate/courses/science/physics/mphys-physics-with-a-year-in-industry-f30y/",
"http://www.swansea.ac.uk/undergraduate/courses/science/physics/bsc-physics-with-particle-physics-and-cosmology-f3f5/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-physics-with-foundation-year-f301/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-physics-with-a-year-abroad-f302/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-politics-l200/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-literature/ba-englitpol-lq23/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-polsocialpol-ll42/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-politicsandwelsh-lq2n/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-politicsandwelsh-lqf5/",
"http://www.swansea.ac.uk/undergraduate/courses/medicine/phms/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonspsychology/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/specialist_community_public_health_nursing/",
"http://www.swansea.ac.uk/humanandhealthsciences/continuing-professional-development/fullawards/specialist_community_public_health_nursing/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/pr-media/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/media-pr-and-communication/pr-media-pp47/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-pure-mathematics-g110/",
"http://www.swansea.ac.uk/rtp/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonssocialpolicy/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonssocialsciences/",
"http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bsc-social-work/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-software-engineering-g600/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/bsc-software-engineering-with-a-year-abroad-c60b/",
"http://www.swansea.ac.uk/undergraduate/courses/science/computer-science/bsc-software-engineering-with-a-year-in-industry-g60a/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/spanish/ba-spanish-r410/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/spanish/ba-spanishandwelsh-qr54/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/bsc-sports-science-c600/",
"http://www.swansea.ac.uk/undergraduate/courses/engineering/bsc-sports-science-c600/bsc-sports-science-c601/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-tesol-qx00/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-tesolenglit-qxh3/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/english-language/ba-tesolenglit-qx01/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-tesolfrench-rx13/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-gertefl-rx23/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-italian-tesoll-rx33/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/tesol/ba-tesolspanish-rx43/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-theoretical-physics-f341/",
"http://www.swansea.ac.uk/undergraduate/courses/science/mphys-theoretical-physics-f340/",
"http://www.swansea.ac.uk/undergraduate/courses/science/physics/bsc-theoretical-physics-with-a-year-in-industry-f636/",
"http://www.swansea.ac.uk/undergraduate/courses/science/physics/mphys-theoretical-physics-with-a-year-in-industry-f857/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/war-and-society/ba-war-l252/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/cymraeg-welsh/cymraeg1stlanguage/ba-cymraeg-q561/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/cymraeg-welsh/cymraegwelsh2ndlanguage/ba-cymraegwelsh-q560/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-historyandwelsh-qv5c/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/history/ba-historyandwelsh-qv51/",
"http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/cymraeg-welsh/cymraegwelsh2ndlanguage/ba-media-welsh/",
"http://www.swansea.ac.uk/undergraduate/courses/science/bsc-zoology-c300/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-zoology-with-a-year-abroad-c301/",
"http://www.swansea.ac.uk/undergraduate/courses/science/biosciences/bsc-zoology-with-a-year-in-industry-c384/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceaudiology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencecardiacphysiology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencenuclearmedicine/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceneurophysiology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceradiotherapyphysics/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcarescienceradiationphysics/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthcaresciencerespiratoryandsleepphysiology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsadultnursingswansea/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsadultnursingcarmarthen/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonschildnursing/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonsmentalhealthnursing/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/maternity-care/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/maternity-care-part-time/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bmidhonsmidwifery/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/mostosteopathy/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/dipheparamedicscience/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonscriminologyandpsychology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/education/bsc-hons-education-and-psychology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonspsychology/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonshealthandsocialcare/",
                  "http://www.swansea.ac.uk/undergraduate/courses/law/bsccriminologysocialpolicy/",
                  "http://www.swansea.ac.uk/undergraduate/courses/artsandhumanities/politics-and-international-relations/ba-polsocialpol-ll42/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonssocialpolicy/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bschonssocialsciences/",
                  "http://www.swansea.ac.uk/undergraduate/courses/human-and-health-sciences/bsc-social-work/",
                  ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # 370
    # print(len(start_urls))

    def parse(self, response):
        item = get_item1(SchoolItem2)
        item['country'] = "England"
        item["website"] = "http://www.swansea.ac.uk/"
        item['university'] = "Swansea University Prifysgol Abertawe"
        item['create_person'] = 'yangyaxia'
        item['url'] = response.url
        print("===============================")
        print(response.url)
        try:
            # 专业、学位类型
            courseDegreeaward = response.xpath("//h1[@class='content-header-heading']//text()").extract()
            courseDegreeawardStr = ''.join(courseDegreeaward)
            if len(courseDegreeawardStr) != 0:
                d = re.findall(r"^(\w+\s/\w+\s/\w+)|^(\w+/\w+/\w+)|(^\w+\s\(\w+\))|^(\w+/\s\w+)|^(\w+)", courseDegreeawardStr)
                if len(d) != 0:
                    degree_type = ''.join(list(d)[0])
                    # print(degree_type)
                    item['degree_type'] = degree_type
                    programme = courseDegreeawardStr.split(degree_type)
                    item['programme'] = ''.join(programme).strip()
            # print("item['degree_type'] = ", item['degree_type'])
            # print("item['programme'] = ", item['programme'])

            # //ul[@style='width: 5000px;']/li[4]
            department = response.xpath(
                "//div[@class='breadCrumb module']//ul/li[4]//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            # print("item['department'] = ", item['department'])

            # ucas_code
            ucas_code = response.xpath(
                "//div[@class='top-button-ucas-code']/div[@class='top-button-value']//text()").extract()
            clear_space(ucas_code)
            item['ucas_code'] = ''.join(ucas_code).strip()
            print("item['ucas_code'] = ", item['ucas_code'])

            # 课程长度
            duration = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/text()").extract()
            clear_space(duration)
            item['duration'] = ''.join(duration).strip()
            # print("item['duration'] = ", item['duration'])

            # mode
            mode = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/small/text()").extract()
            clear_space(mode)
            item['mode'] = ''.join(mode).strip()
            # print("item['mode'] = ", item['mode'])

            # 专业描述
            overview1 = response.xpath(
                "//div[@id='content-items']/div[@class='layout-article-items']/div[@class='title-and-body-text']//text()").extract()
            overview2 = response.xpath("//div[@id='key-features']//text()").extract()
            overview3 = response.xpath("//div[@id='description']//text()").extract()
            clear_space(overview1)
            clear_space(overview2)
            clear_space(overview3)
            overview = '\n'.join(overview1).strip() + "\n" + '\n'.join(overview2).strip() + "\n" +  '\n'.join(overview3).strip()
            item['overview'] = overview.strip()
            # print("item['overview'] = ", item['overview'])

            # 课程设置
            modules = response.xpath("//div[@id='modules']//text()").extract()
            # //div[@id='course-structure-']
            modules1 = response.xpath("//div[@id='course-structure-']//text()").extract()
            # print(modules1)
            clear_space(modules)
            modulesEnd = re.findall(r"\(function\s\(\)\s{.*", '\n'.join(modules).strip())
            # print(modulesEnd)
            clear_space(modules1)
            modules = '\n'.join(modules).strip().strip(''.join(modulesEnd)).strip()
            item['modules'] = modules + '\n'.join(modules1).strip()
            # print("item['modules'] = ", item['modules'])

            # IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            clear_space(entryRequirements)
            item['entry_requirements'] = '\n'.join(entryRequirements).strip()
            # print("item['entry_requirements'] = ", item['entry_requirements'])
            entryRequirementsStr = ''.join(entryRequirements)

            if "Entry Requirements" in entryRequirementsStr:
                alevelStart = entryRequirementsStr.find("Entry Requirements")
                ibStart = entryRequirementsStr.find("International Baccalaureate")
                alevel = entryRequirementsStr[alevelStart:ibStart]
                item['Alevel'] = alevel
            else:
                item['Alevel'] = ""
            ibStart1 = entryRequirementsStr.find("International Baccalaureate")
            if ibStart1 == -1:
                ibStart1 = entryRequirementsStr.find("IB")
            ibEnd = entryRequirementsStr.find("BTEC (18-unit)")
            if ibEnd == -1:
                ibEnd = entryRequirementsStr.find("Welsh")
            ib = entryRequirementsStr[ibStart1:ibEnd - 1]
            item['IB'] = ib
            # print("item['Alevel'] = ", item['Alevel'])
            # print("item['IB'] = ", item['IB'])

            # .{0,100}(IELTS).{0,100}
            # ielts = re.findall(r"\.[a-zA-Z0-9\s.]{0,80}(IELTS)[a-zA-Z0-9\s.\(\))]{0,80}", entryRequirementsStr)
            pat = r".{0,100}IELTS.{0,100}"
            re_ielts = re.compile(pat)
            ielts = re_ielts.findall(entryRequirementsStr)
            item['IELTS'] = ''.join(ielts)
            # print("item['IELTS'] = ", item['IELTS'])
            ielts = item['IELTS']
            ieltlsrw = re.findall(r"\d\.\d", ielts)
            # print(ieltlsrw)
            if len(ieltlsrw) >= 2:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[1]
                item['IELTS_S'] = ieltlsrw[1]
                item['IELTS_R'] = ieltlsrw[1]
                item['IELTS_W'] = ieltlsrw[1]
            elif len(ieltlsrw) == 1:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[0]
                item['IELTS_S'] = ieltlsrw[0]
                item['IELTS_R'] = ieltlsrw[0]
                item['IELTS_W'] = ieltlsrw[0]
            # print(
            #     "item['IELTS'] = %s item['IELTS_L'] = %s item['IELTS_S'] = %s item['IELTS_R'] = %s item['IELTS_W'] = %s " % (
            #     item['IELTS'], item['IELTS_L'], item['IELTS_S'], item['IELTS_R'], item['IELTS_W']))

            # 学费
            # fee = html.xpath("//div[@id='tuition-fees-contents']/div[@class='table-wrapper']/table[@class='expander-item-fees-table']/tbody/tr[@class='expander-item-fees-table-row odd']/td[@class='expander-item-fees-table-data odd'][2]//text()")
            tuition_fee = response.xpath(
                "//div[@id='tuition-fees-contents']//table[@class='expander-item-fees-table']/tbody/tr[1]/td[4]//text()").extract()
            clear_space(tuition_fee)
            item['tuition_fee'] = ''.join(tuition_fee)
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='how-to-apply']
            how_to_apply = response.xpath(
                "//div[@id='how-to-apply']//text()").extract()
            clear_space(how_to_apply)
            item['how_to_apply'] = '\n'.join(how_to_apply).strip()
            # print("item['how_to_apply'] = ", item['how_to_apply'])

            career = response.xpath(
                "//div[@id='careers-and-employability']//text()|//div[@id='careers-employability']//text()|//div[@id='employabilitycareers']//text()|//div[@id='employability-and-careers-']//text()|//div[@id='careers-in-child-nursing-']//text()|//div[@id='careers']//text()|//div[@id='graduate-employability-and-careers']//text()|//div[@id='careers-in-radiotherapy-physics']//text()|//div[@id='careers-in-midwifery']//text()|//div[@id='careers-in-neurophysiology-']//text()|//div[@id='careers-in-psychology-']//text()|//div[@id='careers-in-adult-nursing-']//text()").extract()
            clear_space(career)
            item['career'] = '\n'.join(career).strip()
            # print("item['career'] = ", item['career'])

            item['deadline'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/applying-for-2018/"
            item['interview'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/interviews/"
            item['chinese_requirements'] = """"""
            yield item
        except Exception as e:
            with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
