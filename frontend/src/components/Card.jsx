import { Link } from "react-router-dom";

export default function Card({value}){
    const imgPath = `../images/album_${value.id}.jpg`;
    return (
        <Link to={`collection/${value.id}`}>
        <div className = 'card-div'>
            <img className="thumbnail" src={imgPath}></img>
            <h3>{ value.title }</h3>
        </div>
        </Link>
    );
}