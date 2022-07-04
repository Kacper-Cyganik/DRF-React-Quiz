import Header from "./framework/Header"
import ConnectApi from "../api/ConnectApi"

export const QuizSelect = () => {

    const API_URL = "http://127.0.0.1:8000/api/quiz/"
    const [dataState] = ConnectApi(API_URL)
    console.log(dataState);
    return(
        <div><Header/></div>
    )
}

export default QuizSelect;
