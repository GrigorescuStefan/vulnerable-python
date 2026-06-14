# template_engine.py

def render_template(user_expression, context):
    """
    Safe replacement: only allows simple variable access.
    """

    try:
        # FIX: no eval — only simple lookup
        if user_expression in context:
            return f"Result: {context[user_expression]}"

        return "Unsupported expression"

    except Exception as e:
        return f"Error: {str(e)}"


def calculate_discount(price, discount_factor):
    # FIX: explicit arithmetic instead of eval
    return price * discount_factor