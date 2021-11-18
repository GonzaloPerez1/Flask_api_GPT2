from transformers import pipeline

generator = pipeline("text-generation", model="PlanTL-GOB-ES/gpt2-base-bne")
generator(
    "¿Qué modelo es mejor?",
    max_length=200,
    num_return_sequences=10,
)
