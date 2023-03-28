import pandas as pd
import gradio as gr


def table(file_name, num_rows, quest):
    df = pd.read_csv(file_name)
    df.dropna(axis=0, inplace=True)
    df = df.head(int(num_rows))
    shape = df.shape
    desc = df.describe()
    atribut = shape[1]
    obj = shape[1] * shape[0]
    if quest == "":
        blank = ""
        return df, desc, atribut, obj, blank
    elif quest == "Ile klas decyzyjnych?":
        num_classes = len(df.iloc[:, -1].value_counts())
        return df, desc, atribut, obj, num_classes
    elif quest == "Wielkosc kazdej klasy decyzyjnej?":
        class_sizes = df.iloc[:, -1].value_counts().to_dict()
        return df, desc, atribut, obj, class_sizes
    else:
        return "Jakis blad kolego."


input_file = gr.inputs.Textbox(label="Wprowadz nazwe pliku:")
input_num_rows = gr.inputs.Number(label="Ile wierszy chcesz zobaczyc:")
input_quest = gr.inputs.Dropdown(["Ile klas decyzyjnych?", "Wielkosc kazdej klasy decyzyjnej?"],
                                 label="Wybierz pytanie:")
output_desc = gr.outputs.Textbox(label="Opis tabeli:")
output_df = gr.outputs.Dataframe(label="DataFrame:", type='pandas')
output_atribut = gr.outputs.Textbox(label="Liczba atrybutow:")
output_obj = gr.outputs.Textbox(label="Liczba obiektow:")
output_quest = gr.outputs.Textbox(label="Odp:")

iface = gr.Interface(
    fn=table,
    inputs=[input_file, input_num_rows, input_quest],
    outputs=[output_df, output_desc, output_atribut, output_obj, output_quest],
    title="Chatbocik",
)

iface.launch()
