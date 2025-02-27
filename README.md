# SlackBuilds.org_Dependencies_Graph
visualizes the dependencies between all SlackBuilds scripts using a D3.js force-directed graph. You can explore nodes and their connections, search for specific packages, and interact with the graph to explore dependencies.
---

![image](./image.png)

--- 

[video](https://www.youtube.com/watch?v=Qvsoa1hI_Z8)

---

## BUILD 

`git clone https://github.com/rizitis/SlackBuilds.org_Dependencies_Graph.git` <br>
`cd SlackBuilds.org_Dependencies_Graph` <br>
`npm init -y` <br>
`npm install express axios` <br>

#### Run server
`node server.js`<br>

Open your browser `http://localhost:3000` <br>

To kill server Ctrl+C 

#### Required
`slpkg to be installed, focus to ponce repo and updated`


---

**Alternative** 
<br>if you preffer graphviz just run `python3 python-graph.py`<br>
Output will be a folder: *dependency_graphs* <br>
In there every package has its own .png with all deps, example:<br>
![python3-py7zr](./python3-py7zr_dependencies.png)

[Here](https://github.com/rizitis/SlackBuilds.org_Dependencies_Graph/raw/refs/heads/main/dependency_graphs.tar.gz) is the folder compressed. *(ponce repo 07/02/2025)*

- For easy  images view, you can edit `show-deps` script to correct/fix your DIRPATH (dependency_graphs) and cmd: `bash show-deps <pkg_name>` 

Again requires `slpkg to be installed, focus to ponce repo and updated`



