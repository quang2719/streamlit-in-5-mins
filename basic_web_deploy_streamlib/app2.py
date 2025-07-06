import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io
from PIL import Image
def percentage_distribution(scores):
    bins = {
        '>= 80':0,
        '60-79':0,
        '40-59':0,
        '< 40':0,
    }
    for score in scores:
        if score >= 80:
            bins['>= 80'] +=1
        elif score >= 60:
            bins['60-79'] +=1
        elif score >= 40:
            bins['40-59'] +=1
        else:
            bins['< 40']+=1

    return bins



def main():
    st.title('phan tich diem hoc sinh')
    uploaded_file = st.file_uploader('choose excel file', type = ['xlsx'])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        score = df['Điểm số'].dropna().astype(float).tolist()
        # average
        avg = sum(score)/len(score)
        st.write(f'diem trung binh: {avg}')

        # distribution
        res = percentage_distribution(score)
        st.write(res)

        # show distribution
        fig,ax = plt.subplots(figsize = (1,1))
        labels = list(res.keys())
        values = list(res.values())
        ax.pie(
            values,
            labels = labels,
            autopct = '%1.1f',
            textprops = {'fontsize':3.5}
        )
        ax.axis('equal')
        plt.tight_layout(pad = 0.1)
        buf = io.BytesIO()
        fig.savefig(buf, format = 'png',dpi = 500)
        img = Image.open(buf)
        st.write('bieu do phan bo diem')
        st.image(img)

if __name__ == '__main__':
    main()
