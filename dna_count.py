import pandas as pd
import streamlit as st
import altair as aly

# Page Title

st.write("""
# DNA Nucleotide Count Web App
         (ATCG)
   ***      
    """)

st.header("Enter DNA Sequence")

sequence_input = "DNA Query \n ATCGA \n TCGCGTGG \n ATGCCTAC"

sequence = st.text_area("sequence_input", sequence_input, height =150)
sequence = sequence.splitlines()

sequence = sequence[1:]

sequence = ''.join(sequence) # wrt to wht is in between ''

st.write("""
        ***
        """)

st.header('Input (DNA Query)') # print DNA Sequence
sequence


# DNA Nucleotide count

st.header("Output DNA Nucleotide Count")

st.subheader('Print Dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X