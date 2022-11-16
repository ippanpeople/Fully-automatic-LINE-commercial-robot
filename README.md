# Fully automatic LINE commercial robot

## About this project

## About line-bot-sdk
- Webhook Event Objects
<table rules="none" align="center">
	<td>
        <table rules="none" align="center">
MessageEvent(訊息)
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
FollowEvent(加入, 解除封鎖)
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
                <td>Ｘ</td>
            </tr>    
        </table>
    </td>
	<td>
        <table rules="none" align="center">
UnfollowEvent(封鎖)
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
                <td>Ｘ</td>
            </tr>    
            <tr>
                <td>Ｘ</td>
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