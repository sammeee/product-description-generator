from huggingface_hub import InferenceClient
import os


client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.environ.get("HF_TOKEN")
    )

#Few-Shot: Tones with Examples
FEW_SHOT_EXAMPLES = {
    "professional": """
Product: Noise-Cancelling Headphones
Description: Engineered for the discerning professional, these headphones deliver studio-grade audio clarity with adaptive noise cancellation. Designed for extended wear and seamless connectivity.

Product: Standing Desk
Description: Optimise your workspace with our height-adjustable standing desk. Built from sustainably sourced materials, it supports productivity through ergonomic design and cable management systems.
""",
    "casual": """
Product: Noise-Cancelling Headphones
Description: Block out the world and vibe to your playlist. These headphones are comfy, wireless, and sound absolutely amazing. Perfect for commutes, WFH, or just zoning out.

Product: Standing Desk
Description: Tired of sitting all day? This desk goes up and down so you can stand whenever you feel like it. Super easy to set up and looks great in any room.
""",
    "luxury": """
Product: Noise-Cancelling Headphones
Description: An audiophile experience reimagined. Handcrafted with premium leather and aerospace-grade aluminium, these headphones are the pinnacle of acoustic engineering and refined taste.

Product: Standing Desk
Description: Where form meets function in perfect harmony. Our bespoke standing desk, finished in hand-polished walnut and brushed brass, transforms any workspace into a sanctuary of elegance.
"""
}

def generate_description(product_name:str, tone:str)->str:
    """Generate a product description using few-shot prompting"""

    examples = FEW_SHOT_EXAMPLES.get(tone, FEW_SHOT_EXAMPLES["professional"])
    
    prompt = f"""You are a professional copywriter. Generate a product description in a {tone} tone.
Study these examples carefully and match their style exactly:

{examples}
Now write a description for the following. Output the description only, nothing else.

Product: {product_name}
Description:"""

    response = client.text_generation(
        messages=[{"role":"user","content":prompt}],
        max_tokens=200,
        temperature=0.7
        )

    return response.choices[0].message.content.strip()
