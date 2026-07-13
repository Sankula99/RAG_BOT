import ChatInterface from './components/ChatInterface'
import FileUpload from './components/FileUpload'

function App(){
    return(
        <div className="app">
            <FileUpload/>
            <ChatInterface/>
        </div>
    );
}
export default App;
