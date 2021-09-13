from jinja2 import Template

if __name__ == '__main__':

    tpl_text = '僕の名前は{{ name }}です!! {{ lang }}が好きです!!'
    template = Template(tpl_text)

    data = {'name': 'Kuro', 'lang':'Python'}
    disp_text = template.render(data)
    print(disp_text)
    