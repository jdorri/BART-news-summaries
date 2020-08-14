
class NLP(object):

    MODELS = [
        'facebook/bart-large-cnn'
    ]

    def __init__(self):
        pass
    
    def summarise_with_BART(self, text_block):
        from transformers import BartTokenizer, BartForConditionalGeneration

        tokenizer = BartTokenizer.from_pretrained(NLP.MODELS[0])
        model = BartForConditionalGeneration.from_pretrained(NLP.MODELS[0])

        inputs = tokenizer([text_block], padding=True, truncation=True, max_length=1024,return_tensors="pt")
        outputs = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)

        summary = [tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=False) for output in outputs]

        return summary
    
    def NER_with_SpaCy(self, text_block, query):
        import en_core_web_sm 
        nlp = en_core_web_sm.load()

        doc = nlp(text_block)
        desired_labels = ['PERSON', 'ORG']
        leave_out = [query]
        entities = [ent.text for ent in doc.ents if ent.label_ in desired_labels and ent.text not in leave_out]

        if entities == []:
            key_ents = [(None, None), (None, None)]

        if entities != []:
            from collections import Counter
            key_ents = Counter(entities).most_common(2)

        return key_ents 
    

