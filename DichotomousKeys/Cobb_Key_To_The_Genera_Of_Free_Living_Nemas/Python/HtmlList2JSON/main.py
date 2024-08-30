import requests
from bs4 import BeautifulSoup
import json

# Fetch HTML from a URL
def get_content():
    url = "https://example.com/your-html-page.html"
    response = requests.get(url)
    html_content = response.content

    # Or load HTML from a local file
    fn = '../../WWW3_TreeView.html'
    with open(fn, "r") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    root_list = soup.find("ul")

    return root_list


def html_list_to_json(html_list):
  """Recursively converts a nested HTML list to a JSON structure.
  Args:
    html_list: The BeautifulSoup object representing the HTML list.

  Returns:
    A JSON representation of the nested list.
  """
  json_data = []
  for item in html_list.find_all("li"):
    item_json = {"node": item.text.strip()}
    child_list = item.find("ul") or item.find("ol")  # Check for both <ul> and <ol>
    if child_list:
      item_json["children"] = html_list_to_json(child_list)
    json_data.append(item_json)
  return json_data





def main():
    # Use a breakpoint in the code line below to debug your script.
    root_list = get_content()
    json_result = html_list_to_json(root_list)
    print(json.dumps(json_result, indent=2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



