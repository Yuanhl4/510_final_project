import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pal_index.csv')

st.title('Palworld Pal Stats Calculator')

def calculate_stats(pal_name, level):
    base_stats = df.loc[df['Name'] == pal_name, ['Atk', 'HP', 'Def']].iloc[0]
    stats_growth = {'Atk': 6.5, 'HP': 12.5, 'Def': 5} 
    stats_at_level = {stat: base_val + (level - 1) * growth for stat, (base_val, growth) in zip(base_stats.index, zip(base_stats, stats_growth.values()))}
    return stats_at_level

selected_pal = st.selectbox('Select the 1st Pal', ['Choose a Pal'] + list(df['Name'].unique()))
comparison_pal = st.selectbox('Select the 2nd Pal', ['Choose a Pal'] + list(df['Name'].unique()))

if selected_pal != 'Choose a Pal' or comparison_pal != 'Choose a Pal':
    level = st.slider('Select Level', 1, 50, 25)
    if selected_pal != 'Choose a Pal':
        selected_stats = calculate_stats(selected_pal, level)
        st.write(f"Stats for {selected_pal} at level {level}:")
        st.write(selected_stats)
    if comparison_pal != 'Choose a Pal':
        comparison_stats = calculate_stats(comparison_pal, level)
        st.write(f"Stats for {comparison_pal} at level {level}:")
        st.write(comparison_stats)

    fig, ax = plt.subplots()
    if selected_pal != 'Choose a Pal':
        ax.bar(selected_stats.keys(), selected_stats.values(), width=-0.4, align='edge', label=selected_pal)
    if comparison_pal != 'Choose a Pal' and comparison_pal != selected_pal:
        ax.bar(comparison_stats.keys(), comparison_stats.values(), width=0.4, align='edge', label=comparison_pal)

    ax.set_ylabel('Value')
    ax.set_title('Stats Comparison at Level {}'.format(level))
    ax.legend()
    st.pyplot(fig)
else:
    st.write('Please select at least one Pal to display stats and comparison.')