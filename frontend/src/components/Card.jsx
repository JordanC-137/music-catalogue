import { Link } from "react-router-dom";

export default function Card({value}){
    return (
        <Link to={`collection/${value.id}`}>
        <div className = 'card-div'>
            <h3>{ value.title }</h3>
        </div>
        </Link>
    );
}