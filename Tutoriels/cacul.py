def addition() :
    result = 65 + 5
    return result


# autre méthode du renvois du résultat
def multiply():
    return 15 * 5


def get_message():
    return "Le résultat du calcule est "


print(get_message(), addition())
print(get_message(), multiply())
