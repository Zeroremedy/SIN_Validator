def luhn_check(sin: str) -> bool:
    """
    Validate a SIN using the Luhn algorithm.
    """
    digits = [int(d) for d in sin if d.isdigit()]
    if len(digits) != 9:
        return False

    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit
    return total % 10 == 0


def generate_valid_sins_with_prefix(prefix: str, count: int = 10) -> list[str]:
    """
    Generate a list of valid SINs starting with the given prefix.
    """
    if not prefix.isdigit() or len(prefix) >= 9:
        raise ValueError("Prefix must be numeric and less than 9 digits long.")

    valid_sins = []
    remaining_digits = 9 - len(prefix)

    for i in range(10**remaining_digits):
        candidate = f"{prefix}{i:0{remaining_digits}d}"
        if luhn_check(candidate):
            formatted = f"{candidate[:3]} {candidate[3:6]} {candidate[6:]}"
            valid_sins.append(formatted)
            if len(valid_sins) >= count:
                break

    return valid_sins

prefix = input("Enter a SIN prefix (1 to 8 digits): ").strip()
if not prefix:
    print("Error: No prefix provided.")
else:
    count_input = input("How many valid SINs to generate? (default 10): ").strip()
    count = int(count_input) if count_input.isdigit() else 10

    try:
        results = generate_valid_sins_with_prefix(prefix, count)
        if results:
            print("\nValid SINs with prefix", prefix)
            for sin in results:
                print(sin)
        else:
            print("No valid SINs found with this prefix.")
    except ValueError as e:
        print("Error:", e)
