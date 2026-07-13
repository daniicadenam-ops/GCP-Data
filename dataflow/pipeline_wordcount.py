import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # Configuración del pipeline
    options = PipelineOptions(
    #    runner="DirectRunner",  # para correr local
        runner="DataflowRunner",  # Cambiar a DataflowRunner para GCP en dataflow
        project="gcp-data-engineer-03-502218",
        region="us-east1",
        temp_location="gs://gcs-bucket-03/temp"
    )

    with beam.Pipeline(options=options) as p:
        (p
         | "Leer archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
         | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
         | "Contar palabras" >> beam.combiners.Count.PerElement()
         | "Guardar resultados" >> beam.io.WriteToText("gs://gcs-bucket-03/output/wordcount")
        )
print("Pipeline ejecutado correctamente.")

if __name__ == "__main__":
    run()
