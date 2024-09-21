import { Link } from "react-router-dom";
import './Card.css';


export default function Card({value}){
    const imgPath = `../images/album_${value.id}.jpg`;
    return (
        <Link className="card-link" to={`collection/${value.id}`}>
        <div className = 'card-div'>
            <img className="card-thumbnail" src={imgPath}></img>
            <p className="card-title">{ value.title }</p>
        </div>
        </Link>
    );
}