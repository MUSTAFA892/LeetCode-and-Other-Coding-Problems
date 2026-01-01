class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()

        for i in range(len(sentence)):
            value = sentence[i]

            try:
                int(value[1:])
                price = int(value[1:])
                        
                if value[0] == '$':
                    final = price * (100 - discount) / 100
                    value_updation = str('$'+str(final))

                    if '.' in value_updation:
                        decimal_part = value_updation.split('.')[-1]
                        if len(decimal_part) == 1:
                            value_updation += '0'
                            
                    else:
                        value_updation += '.00'
                    sentence[i] = value_updation
                    
            except ValueError:
    
                continue

        return " ".join(sentence)