import markdown


lines = []
current_section = ''
title = ''
description = []
image = ''
tips = []
ingredients = []
steps = []

with open('spanish_rice.md', 'r') as f:
    lines = f.readlines()

for line in lines:
    # print(f'line: {line}')
    if line.startswith('## '):
        # print(f"line.strip().lstrip('## '): *{line.strip('## ')}*")
        current_section = line.strip().lstrip('## ')
        # print(f'New current_section: {current_section}')
    else:
        if line.strip() == '':
            continue

        if current_section == 'Title':
            title = line.strip()
        elif current_section == 'Description':
            description.append(line)
        elif current_section == 'Image':
            image = line.strip()
        elif current_section == 'Tips':
            tips.append(line)
        elif current_section == 'Ingredients':
            ingredients.append(line.strip())
        elif current_section == 'Steps':
            steps.append(line.strip())

print(f'Title: {title}')
print(f'Description: {description}')
print(f'Image: {image}')
print(f'Tips: {tips}')
print(f'Ingredients: {ingredients}')
print(f'Steps: {steps}')
print(markdown.markdown('\n'.join(steps)))

with open('spanish_rice.html', 'w') as f:
    f.write('{% extends "recipe.html" %}\n')
    f.write('\n')

    f.write('{% block recipe_title %}\n')
    f.write(f'<h1>{title}</h1>\n')
    f.write('{% endblock %}\n')
    f.write('\n')

    f.write('{% block recipe_description %}\n')
    f.write('<h2>Description</h2>\n')
    f.write(markdown.markdown('\n'.join(description)))
    f.write('\n{% endblock %}\n')
    f.write('\n')

    f.write('{% block recipe_image %}\n')
    f.write(f'{image}\n')
    f.write('{% endblock %}\n')
    f.write('\n')

    f.write('{% block recipe_tips %}\n')
    f.write('<h2>Tips</h2>\n')
    f.write(markdown.markdown('\n'.join(tips)))
    f.write('\n{% endblock %}\n')
    f.write('\n')

    f.write('{% block recipe_ingredients %}\n')
    f.write('<h2>List of Ingredients</h2>\n')
    f.write(markdown.markdown('\n'.join(ingredients)))
    f.write('\n{% endblock %}\n')
    f.write('\n')

    f.write('{% block recipe_steps %}\n')
    f.write('<h2>Recipe Steps</h2>\n')
    f.write(markdown.markdown('\n'.join(steps)))
    f.write('\n{% endblock %}\n')
