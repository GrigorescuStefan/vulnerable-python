# template_engine.py

def render_template(user_expression, context):
    """
    Very naive template engine used for demo purposes.
    """

    # VULNERABILITY: unsafe eval
    try:
        result = eval(user_expression, {"__builtins__": {}}, context)
        return f"Result: {result}"
    except Exception as e:
        return f"Error rendering template: {str(e)}"


def calculate_discount(price, discount_expr):
    # e.g. "price * 0.9"
    return eval(discount_expr)