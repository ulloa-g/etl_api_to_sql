from extract import extract_data


def transform_data():
    df = extract_data()
    df['fecha'] = df['fecha_hora'].dt.strftime('%d/%m/%Y')
    df['hora'] = df['fecha_hora'].dt.strftime('%H:%M')
    df = df.drop(columns=['fecha_hora'])
    df = df[['fecha', 'hora', 'pais', 'ciudad', 'temp_actual',
            'sensacion_termica', 'clima', 'descripcion_clima',
            'temp_min', 'temp_max', 'velocidad_viento[m/s]']]
    return df


cleaned_df = transform_data()
