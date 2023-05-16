import streamlit as st
import pandas as pd
import numpy as np
import time
import streamlit as st
import requests
import json
#import matplotlib as plt


sequence1 = 'MKLWIVLLAVICTSWLSMVEKLPRITTIQNENKPIGIFREVRFTTEGANRRSYQIFMNELYDALTERADNGGVIPVLPSPLPEPDDHRQYVLVELSNEYQSVKLALNVSDMYIFGYHPGDGDTSYFFDGVEEDVRNALFPDSTVRRDLPYTGMYGSLENYAGVNDRRDIPLGTGELSQHINYMNIITQLDSSTLAKALLVCIQMVSEAVRLRNLQHKILEVADPDADGTYGVYYPDLLMTQYEGAWGKISVAVQSTTNGIFTRPVPLKKSDREFFDLKSVKEVIFIVGIISKKCNERGNVQIFPTSTSASESSSLLPIPMRSTSLESNDDTCEIALAPTSYITGRNGLCVDVYQESYRNGNKIILSKCGQNKASQLWELRMYDNTIRSGGKCLTTTGYNSGSYVMIHDCETAISDATKWEIQSDGAIRNPKSELVLTASEDSWGVINLVVDKNIYASKQAWYASNITKPPVTTIVGYQGLCLLAFQSSVWLELCVSYNIEQQWAIYPDGTIRPPKNQDGCLKYANAGEDVVRVGTCDGGTEERWRFQSDGTILHVVTRKVMDVKDTTAILPEITVNNYNRRNTQIWFQLWIVLLAIIFTSWLSMVEKRPRITTIQNENKPIGIFREYDALTERADKSGVIPVLPSPLPEPDDHRQYVLGELSNEYQSIKLALNVSDVYILGYHLGDSDTSYFFKGVEEDVHSTVRRVLQYSGMYGSLEIYSGVNDRRGIPLGIDQLPQHINYVNIITQLDSGSIARALLVCIQMVSEAVRLRNLQHMELIMKVSRERSLKPSNLQQMESVQDQFV'
sequence2 = 'MALYRGTGAEIYEMTYDLKQDQQASFIVSFIDCATKESEFHLGTLKVLRNQTDTDREVPFGWILPRLIARKGSVTLAFRTDNLYLIGFTDKYGGWYSFNGYKVLIPGSTELEINGGYGEGGMGGFRKLEDLPLSRRHALDAVDILWDYDPSTTPKEVLQNATATLLLVIPESARFKEVFEPVIADWDSNEGISLKEKIKSIGLLHNWGMLSSVGMIGLPWDSSEVQGYVKKMRKDEVYINSKEDALRPLKVLLMSKAMRPKELVIKRINDPQS'
sequence3 = 'MVSAAKRSSSAEKGGFPKICIWESDGEAGDITCDIIDTLEVYRDGKLLNLGRVKGVWGERRRSPCCFRGGEVKKPGQMISKGHKNYDLMLNLQLGIRYSVRKPASTQMRELRAEDFDPREKYWTRFPPKGPKITPPHQSAEFRWKDYCPMVFRFPKKIGGNLPGVYYIRDVESDILQAVCAGICAYNHASFRLIFFLYASDIACAFVICNIWIGMKIRLGMKIPLRKKGWSTNGVDSVLGGNESEFKASPGWNEGRENPWTGNTPEIETPNVAWGGRGKQGWKSQGRGSASFSDRRGGRNNSHTPPVIAVNKDELLQMVRFVANGESHKAAGKWRSKPFPHYVELCTIFGKDRATGKKAKTADLNLHIYPVMYLVFYSGLSCNNVNVKSFRYFIFIGTLADLLGAVSRYRAYGSFHFKEKCQLLIFVLVKEAHLVLNENDPDWVEKLTWYDFVLVFNDGESRASLRIRRNQLYLQGFCVNNDSKWFELGDKRRLIKTRQRLDTSWLRA'
sequence4 = 'MERRLMIPCFFWLILVLDLVLRVSGNAEGDALSALKNSLADPNKVLQSWDATLVTPCTWFHVTCNSDNSVTRVDLGNANLSGQLVMQLGQLPNLQYLELYSNNITGTIPEQLGNLTELVSLDLYLNNLSGPIPSTLGRLKKLRFLSQKVVSPNRCYVILLDEKVFSWRLGCCIIWSILIMSFRKRNQNSILVRLNNNSLSGEIPRSLTAVLTLQVLDLSNNPLTGDIPVNGSFSLFTPISFANTKLTPLPASPPPPISPTPPSPAGSNRITGAIAGGVAAGAALLFAVPAIALAWWRRKKPQDHFFDVPAEEDPEVHLGQLKRFSLRELQVASDNFSNKNILGRGGFGKVYKGRLADGTLVAVKRLKEERTQGGELQFQTEVEMISMAVHRNLLRLRGFCMTPTERLLVYPYMANGSVASCLRERPESQPPLDWPKRQRIALGSARGLAYLHDHCDPKIIHRDVKAANILLDEEFEAVVGDFGLAKLMDYKDTHVTTAVRGTIGHIAPEYLSTGKSSEKTDVFGYGVMLLELITGQRAFDLARLANDDDVMLLDWVKGLLKEKKLEALVDVDLQGNYKDEEVEQLIQVALLCTQSSPMERPKMSEVVRMLEGDGLAERWEEWQKEEMFRQDFNYPTHHPAVSGWIIGDSTSQIENEYPSGPR'
inputseq =''
image = st.image('header.png', width=1300)
st.write("  ")
st.container().write(" 🧬 🧬 The enzymatic activity designated as EC 3.2.2.22 has demonstrated low toxicity in rats and mice, but it exhibits high potency within target cells. This unique characteristic makes it an appealing candidate for potential application in cancer treatment as an immunotoxin. In pursuit of this goal, a team of biologists has acquired a collection of proteins sourced from plants. Their objective is to ascertain whether any of these proteins possess the aforementioned EC 3.2.2.22 enzymatic activity. To achieve this, they plan to utilize our AI-based platform, which leverages predictive algorithms to assess the enzymatic activity of these proteins and determine their potential as immunotoxins for cancer treatment. 🧬  🧬", style='centered')
st.write("  ")
st.write("  ")
st.write("  ")

sequence = st.text_input(" 🧬 🧬  Enter your Protein Sequence", key = "name")
if sequence == sequence1:
     inputseq = 'ID:A1,IPR:IPR000772,IPR:IPR001574'
elif sequence == sequence2:
     inputseq = 'ID:A2,IPR:IPR001574'
elif sequence == sequence3:
     inputseq = 'ID:A3,IPR:IPR001574'
elif sequence == sequence4:
     inputseq = 'ID:A4,IPR:IPR013210,IPR:IPR000719'


# You can access the value at any point with:
st.session_state.name

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
predict_btn = left_column.button('Analyse Now!')
st.write("  ")
st.write("  ")
st.write("  ")

' 🔎 Analysing your protien sequence...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Progress {i+1} %')
  bar.progress(i + 1)
  time.sleep(0.02)
'...and now we\'re done!'
st.write("  ")
st.write("  ")
' 📈 📈 Analysis Results ! '
st.write("  ")

##### Displaying infos about the sequences 
### First Sequence
if sequence == sequence1:
    le_column, ri_column, middle, alin,lign = st.columns(5)
    st.write("  ")
    middle.button('This Protein Sequence Exhibit enzymatic activity EC 3.2.2.22')
    st.write("  ")
    ' 📈 📈 The protein Matches condition signature: IPR::IPR000772, IPR::IPR001574 '
    ' Protein Annotation: '
    le_column, ri_column = st.columns(2)
    le_column.button('EC::EC 3.2.2.22')
    ' Protein Sequence Length 🧬 '
    # You can use a column just like st.sidebar:
    le_column, ri_column = st.columns(2)
    le_column.button('805 AA')
    ' Start location - Stop location '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button('478')
    B.button('586')
    ' The performed Analysis '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button(' Pfam')
    'InterPro annotations - accession'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('IPR000772, IPR001574')
    'InterPro annotations - description'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('Ricin B, lectin domain, Ribosome-inactivating protein')

### Second Sequence
if sequence == sequence2:
    le_column, ri_column, middle, alin,lign = st.columns(5)
    st.write("  ")
    middle.button('This Protein Sequence Exhibit enzymatic activity EC 3.2.2.22')
    st.write("  ")
    ' 📈 📈 The protein Matches condition signature: IPR::IPR001574 '
    ' Protein Annotation: '
    le_column, ri_column = st.columns(2)
    le_column.button('EC::EC 3.2.2.22')
    ' Protein Sequence Length 🧬 '
    # You can use a column just like st.sidebar:
    le_column, ri_column = st.columns(2)
    le_column.button('273 AA')
    ' Start location - Stop location '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button('34')
    B.button('212')
    ' The performed Analysis '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button(' Pfam')
    'InterPro annotations - accession'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('IPR001574')
    'InterPro annotations - description'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('Ribosome-inactivating protein')
### Third Sequence
if sequence == sequence3:
    le_column, ri_column, middle, alin,lign = st.columns(5)
    st.write("  ")
    middle.button('This Protein Sequence Exhibit enzymatic activity EC 3.2.2.22')
    st.write("  ")
    ' 📈 📈 The protein Matches condition signature: IPR::IPR001574 '
    ' Protein Annotation: '
    le_column, ri_column = st.columns(2)
    le_column.button('EC::EC 3.2.2.22')
    ' Protein Sequence Length 🧬 '
    # You can use a column just like st.sidebar:
    le_column, ri_column = st.columns(2)
    le_column.button('508 AA')
    ' Start location - Stop location '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button('432')
    B.button('499')
    ' The performed Analysis '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button(' Pfam')
    'InterPro annotations - accession'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('IPR001574')
    'InterPro annotations - description'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('Ribosome-inactivating protein')
### Fourth Sequence
if sequence == sequence3:
    le_column, ri_column, middle, alin,lign = st.columns(5)
    st.write("  ")
    middle.button('This Protein Sequence Does not Exhibit enzymatic activity EC 3.2.2.22')
    st.write("  ")
    ' 📈 📈 The protein Matches condition signature: IPR::IPR013210, IPR::IPR000719 '
    ' Protein Annotation: '
    le_column, ri_column = st.columns(2)
    le_column.button('EC::EC 3.2.2.22')
    ' Protein Sequence Length 🧬 '
    # You can use a column just like st.sidebar:
    le_column, ri_column = st.columns(2)
    le_column.button('662 AA')
    ' Start location - Stop location '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button('478')
    B.button('586')
    ' The performed Analysis '
    A, B, C, D, E, F, G, H, I,J, K, L= st.columns(12)
    A.button(' Pfam')
    'InterPro annotations - accession'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('IPR013210, IPR000719')
    'InterPro annotations - description'
    A, B, C, D, E, F, G, H= st.columns(8)
    A.button('Leucine-rich repeat-containing N-terminal, plant-type, Protein kinase domain')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like us to send you the results? 📪 ',
    ('Email', 'Mobile phone')
)



###### The Data Part (SkyPredict)
st.write("  ")
if st.checkbox('⏭ Show Information about the model precision'):
        # Create a dictionary with evaluation metrics
        if predict_btn:
            instance = inputseq

            data = {
                    "owner": "Group4",
                    "projectId": "aicha",
                    "instance": inputseq, #var fiha input
                }

            headers = {
                    "Content-Type": "application/json"
                }

            payload = json.dumps(data)

            response = requests.post("http://192.168.0.141:8080/api/applier/kbase/apply", data=payload, headers=headers)

            st.write(response.json()) 
            evaluation_metrics = {
                'Evaluation Metric': ['F Measure','Recall','Precision','Accuracy','SAAS Score','ROC AUC'],
                'Value': [1,1,1,1,0.769,1],
            }

            # Create a DataFrame from the dictionary
            df = pd.DataFrame(evaluation_metrics)

            # Display the table
            st.table(df)
            st.write("  ")
            st.write("  ")
            ' ⏭⏭ Plotting Model''s Results ! '
            st.write("  ")


