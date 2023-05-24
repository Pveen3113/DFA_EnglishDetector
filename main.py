# streamlit run --server.enableCORS false main.py
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
from PIL import Image

#This class is to build the DFA of the English Conjunction Detector
class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
                       'q15',
                       'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28',
                       'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41',
                       'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54',
                       'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67',
                       'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74', 'q75', 'q76', 'q77', 'q78',
                       'trap'}  # set of all states

        self.accept_states = {'q5', 'q7', 'q12', 'q14', 'q15', 'q22', 'q24', 'q27', 'q37', 'q42',
                              'q48', 'q50', 'q55', 'q60', 'q63', 'q65', 'q70', 'q71', 'q75',
                              'q78'}  # set of accept states
        self.transition = \
            {'q0': {'a': 'q1', 'b': 'q16', 'f': 'q25', 'h': 'q38', 'i': 'q49', 'n': 'q61', 'o': 'q64', 's': 'q66',
                    't': 'q72', 'y': 'q76'},
             'q1': {'f': 'q2', 'l': 'q6', 'n': 'q13', 's': 'q15'},
             'q2': {'t': 'q3'},
             'q3': {'e': 'q4'},
             'q4': {'r': 'q5'},
             'q6': {'t': 'q7'},
             'q7': {'h': 'q8'},
             'q8': {'o': 'q9'},
             'q9': {'u': 'q10'},
             'q10': {'g': 'q11'},
             'q11': {'h': 'q12'},
             'q13': {'d': 'q14'},

             # words that start with b
             'q16': {'e': 'q17', 'u': 'q23'},
             'q17': {'c': 'q18'},
             'q18': {'a': 'q19'},
             'q19': {'u': 'q20'},
             'q20': {'s': 'q21'},
             'q21': {'e': 'q22'},
             'q23': {'t': 'q24'},

             # words that start with f
             'q25': {'o': 'q26', 'u': 'q28'},
             'q26': {'r': 'q27'},
             'q28': {'r': 'q29'},
             'q29': {'t': 'q30'},
             'q30': {'h': 'q31'},
             'q31': {'e': 'q32'},
             'q32': {'r': 'q33'},
             'q33': {'m': 'q34'},
             'q34': {'o': 'q35'},
             'q35': {'r': 'q36'},
             'q36': {'e': 'q37'},

             # words that start with h
             'q38': {'e': 'q39', 'o': 'q43'},
             'q39': {'n': 'q40'},
             'q40': {'c': 'q41'},
             'q41': {'e': 'q42'},
             'q43': {'w': 'q44'},
             'q44': {'e': 'q45'},
             'q45': {'v': 'q46'},
             'q46': {'e': 'q47'},
             'q47': {'r': 'q48'},

             # words that start with i
             'q49': {'f': 'q50', 'n': 'q51'},
             'q51': {'d': 'q52', 's': 'q56'},
             'q52': {'e': 'q53'},
             'q53': {'e': 'q54'},
             'q54': {'d': 'q55'},
             'q56': {'t': 'q57'},
             'q57': {'e': 'q58'},
             'q58': {'a': 'q59'},
             'q59': {'d': 'q60'},

             # words that start with n
             'q61': {'o': 'q62'},
             'q62': {'r': 'q63'},

             # words that start with o
             'q64': {'r': 'q65'},

             # words that start with s
             'q66': {'i': 'q67', 'o': 'q71'},
             'q67': {'n': 'q68'},
             'q68': {'c': 'q69'},
             'q69': {'e': 'q70'},

             # words that start with t
             'q72': {'h': 'q73'},
             'q73': {'u': 'q74'},
             'q74': {'s': 'q75'},
             'q76': {'e': 'q77'},
             'q77': {'t': 'q78'},

             # Trap state to accept all inputs that do not have a transition
             'trap': {char: 'trap' for char in 'abcdefghijklmnopqrstuvwxyz'}}  # transition function
        self.current_state = 'q0'  # start state

    #This function is to receive the word and tokenize it to extract each character.
    #The characters are then used for transition in the DFA to and return the boolean staus
    # based on the ending state wheter it is accepting or rejecting state.
    def validate_input(self, input_string):
        for word in input_string:
            if word not in self.transition[self.current_state]:
                self.current_state = 'trap' #trap state if there are no valid transition
                return False  # reject if input symbol is not valid for current state
            self.current_state = self.transition[self.current_state][word]
        if self.current_state in self.accept_states:
            return True  # accept if the final state is an accept state
        else:
            return False  # reject if the final state is not an accept state


#This is to pass the word to the DFA to see wheter the string is accepted or rejected
def dFAWords(word):
    dfa = DFA()
    try:
        if (dfa.validate_input(word)):
            return True
    except:
        return False

#This function is used to store the positions of the strings  that is accepted by the DFA in the input text.
def identify_words(text, words_to_identify):
    word_positions = {}
    words = text.split()
    for index, word in enumerate(words):
        if word in words_to_identify:
            if word not in word_positions:
                word_positions[word] = [index+1]
            else:
                word_positions[word].append(index+1)
    return word_positions

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)


st.title('English Conjunction Detector ☌')
st.caption('Detects all type of coodinating conjunction, certain conjunctive in adverb and subordicating conjunction')

genre = st.radio(
    "Choose an option mode below",
    ('Upload File', 'Check Word'))

if genre == 'Upload File':
    #Initialise a dictionary to store the accepted words with the number of occurance that the word is found
    #in the text input
    my_dict = {}
    total_words = 0
    total_conjunctions = 0
    conjunction = []
    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload the Text File")

    # If a file was uploaded
    if uploaded_file is not None:
        st.subheader('The Text 📄')
        st.caption('The highlights in the text indicates the conjuctions found in the textfile ')
        # Open the uploaded file for reading
        with uploaded_file:
            # Read the contents of the file
            contents = uploaded_file.read().decode('utf-8')
            originalContents = contents
            # Split the contents into lines
            lines = contents.split("\n")
            # Loop over each line
            for line in lines:
                # Split the line into words
                words = line.split()
                # Loop over each word and display it in the app
                for word in words:
                    total_words = total_words + 1
                    if (dFAWords(word.lower())):
                        total_conjunctions = total_conjunctions+1
                        if word.lower() not in conjunction:
                            conjunction.append(word.lower())

                        if word in my_dict:
                            my_dict[word] = my_dict.get(word) + 1
                        else:
                            my_dict[word] = 1
                        contents = contents.replace(" " + word + " ",
                                                    f"<mark style='background-color: yellow'>{word}</mark>")

            word_loc = identify_words(originalContents, my_dict.keys())
            st.write(contents, unsafe_allow_html=True)


        wordOccurnaceTable = []
        for key in my_dict:
            wordOccurnaceTable.append([key, my_dict[key]])

        word_loc_table = []
        for key in word_loc:
            word_loc_table.append([key, word_loc[key]])


        # Convert the data to a DataFrame
        df = pd.DataFrame(wordOccurnaceTable, columns=['Word', 'Count'])

        # Convert the data to a DataFrame
        df_word_loc = pd.DataFrame(word_loc_table, columns=['Word', 'Locations'])

        # CSS to inject contained in a string
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        # Display the DataFrame as a table
        st.subheader('Conjunction Count 🔢')
        st.table(df)
        st.subheader('Conjunction Location 📍')
        st.table(df_word_loc)

        col1, col2, col3 = st.columns(3)
        col1.metric("Words", total_words )
        col2.metric("Highlighted Words", total_conjunctions)
        col3.metric("Conjunction", len(conjunction))

        ColourWidgetText('Words', '#00B0F0')
        ColourWidgetText('Highlighted Words', '#FFFF00')
        ColourWidgetText('Conjunction', '#00FF00')

else:
    st.subheader('Word Input 📄')
    title = st.text_input('Please Input The String', '')
    if(title==''):
        st.write()
    else:
        if(dFAWords(title.lower())):
            #st.write('The string ', title, 'is accepted')
            st.success('This is a Conjunction', icon="✅")
        else:
            #st.write('The string ', title, 'is not accepted')
            st.error('This is NOT a Conjuction', icon="❌")

    DFA_view_option = st.selectbox(
        'Do you want to view the DFA graph',
        ('No', 'Yes'))
    if(DFA_view_option =='Yes'):
        image = Image.open('Automata.png')
        st.image(image, caption='DFA of English Conjunction')
    else:
        st.write()












