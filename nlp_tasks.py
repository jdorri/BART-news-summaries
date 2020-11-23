
class NLP(object):
    """
    A class for downstream NLP tasks: summarisation 
    and entity extraction. 
    """

    MODELS = [
        'facebook/bart-large-cnn' # feel free to try out the newer "distil" models for faster inference
    ]

    def __init__(self):
        pass
    
    def summarise_with_BART(self, text_block):
        """
        Summarisation as conditional language generation.

        See https://huggingface.co for further info on
        using BART models with Hugging Face.

        Args:
            text_block (str): scraped article 
        Returns:
            summary (str): article summary 
        """
        from transformers import BartTokenizer, BartForConditionalGeneration

        tokenizer = BartTokenizer.from_pretrained(NLP.MODELS[0])
        model = BartForConditionalGeneration.from_pretrained(NLP.MODELS[0])

        inputs = tokenizer([text_block], padding=True, truncation=True, max_length=512,return_tensors="pt") # change max_length for shorter summaries
        outputs = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)

        summary = [tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=False) for output in outputs]

        return summary
    
    def NER_with_SpaCy(self, text_block, query):
        """
        Lightweight NER with SpaCy.

        Args:
            text_block (str): scraped article 
        Returns:
            key ent (list): ent data, where
            each elem is of the form (entity, count)
        """
        import en_core_web_sm 
        nlp = en_core_web_sm.load()

        doc = nlp(text_block)
        desired_labels = ['PERSON', 'ORG', 'NORP']
        leave_out = [query]
        entities = [ent.text for ent in doc.ents if ent.label_ in desired_labels and ent.text not in leave_out]

        if entities == []:
            key_ent = [(None, None)]

        if entities != []:
            from collections import Counter
            key_ent = Counter(entities).most_common(1) # we only show one entity in this Proof-of-Concept

        return key_ent
    

