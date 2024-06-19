import React, { useState, useCallback, useEffect } from 'react';
import useWebSocket, { ReadyState } from 'react-use-websocket';
import { DataGrid, useGridApiRef } from '@mui/x-data-grid';

const WS_URL = 'ws://127.0.0.1:8000/ws';

// これを参考に
// https://mui.com/x/react-data-grid/row-updates/#the-updaterows-method

function App() {
  //Public API that will echo messages sent to it back to the client
  const [socketUrl, setSocketUrl] = useState(WS_URL);
  const [messageHistory, setMessageHistory] = useState([]);
  const [rows, setRows] = useState([]);

  const { sendMessage, lastJsonMessage, readyState } = useWebSocket(socketUrl);

  // 受信したデータを設定する
  useEffect(() => {
    if (lastJsonMessage !== null) {
      setMessageHistory((prev) => {
        for (let i = 0; i < prev.length; i++) {
          if (prev[i].id === lastJsonMessage.id) {
            return prev;
          }
        }
        prev.push(lastJsonMessage);
        return prev;
      })
    }
  }, [lastJsonMessage]);

  useEffect(() => {
    setRows([...messageHistory]);
  }, [lastJsonMessage])

  const handleClickChangeSocketUrl = useCallback(
    () => setSocketUrl(WS_URL),
    []
  );

  const handleClickSendMessage = useCallback(() => sendMessage('Hello'), []);

  const connectionStatus = {
    [ReadyState.CONNECTING]: 'Connecting',
    [ReadyState.OPEN]: 'Open',
    [ReadyState.CLOSING]: 'Closing',
    [ReadyState.CLOSED]: 'Closed',
    [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
  }[readyState];
  
  const columns = [
    { field: 'id', headerName: 'id', width: 150 },
    { field: 'severity', headerName: 'Severity', width: 150 },
    { field: "message", headerName: "Message", width: 300}
  ];

  return (
    
    <div>
        <div style={{ height: 300, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} />
    </div>
      <button onClick={handleClickChangeSocketUrl}>
        Click Me to change Socket Url
      </button>
      <button
        onClick={handleClickSendMessage}
        disabled={readyState !== ReadyState.OPEN}
      >
        Click Me to send 'Hello'
      </button>
      <span>The WebSocket is currently {connectionStatus}</span>
      {lastJsonMessage ? <span>Last message: {lastJsonMessage.data}</span> : null}
      <ul>
        {
          messageHistory.map((message, idx) => {
          return (<li key={idx}><span key={idx}>{message ? message.message : null}</span></li>)
          })
        }
      </ul>
    </div>
  );
};

export default App
