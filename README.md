# Fully automatic LINE commercial robot

## About this project

## About line-bot-sdk
### Webhook Event Objects
<table rules="none" align="center">
	<td>
        <table rules="none" align="center">
- MessageEvent(訊息)
            <tr>
                <td>type</td>
            </tr>
            <tr>
                <td>mode</td>
            </tr>
            <tr>
                <td>timestamp</td>
            </tr>
            <tr>
                <td>source:Source</td>
            </tr>    
            <tr>
                <td>reply_token</td>
            </tr>    
            <tr>
                <td>message:Message</td>
            </tr>    
        </table>
    </td>
	<td>
        <table rules="none" align="center">
- FollowEvent
            <tr>
                <td>OS</td>
                <td>CentOS7</td>
            </tr>
            <tr>
                <td>CPU</td>
                <td>2 Core</td>
            </tr>
            <tr>
                <td>RAM</td>
                <td>2 G</td>
            </tr>
            <tr>
                <td>Disk</td>
                <td>10 G</td>
            </tr>
        </table>
    </td>
	<td>
        <table rules="none" align="center">
- サーバ設定
            <tr>
                <td>Domain</td>
                <td>devre.rinlink.jp</td>
            </tr>
            <tr>
                <td>WebServer</td>
                <td>apache</td>
            </tr>            
            <tr>
                <td>node.js</td>
                <td>16.17.1</td>
            </tr>
            <tr>
                <td>React</td>
                <td>17.0.2</td>
            </tr>  
        </table>
    </td>
</table>


## How to use
1. use Dockerfile build env image
```bash
docker build -t rakunabe .
```
2. create project file
```bash
mkdir app.py
```
3. run your project in the container 
```bash
docker run --name rakunabe -p 5002:5002 --restart=always -v /root/Fully-automatic-LINE-commercial-robot:/app -d rakunabe
```