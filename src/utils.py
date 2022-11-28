class Utils:
    def check_requirements(requirements):
        if 'you_or_thou' in requirements:
            you_or_thou = requirements['you_or_thou']
            if you_or_thou not in ('you', 'thou'):
                raise Exception(f"{you_or_thou} is invalid. Use 'you' or 'thou'")
        if 'tone' in requirements:
            if requirements['tone'] not in ('positive', 'negative', 'neutral'):
                raise Exception(f"Invalid tone: {requirements['tone']}")