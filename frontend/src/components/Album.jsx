import { useLoaderData } from "react-router-dom";
import axios from 'axios';

export async function loader({params}){
    const url = `http://127.0.0.1:8000/collection/${params.id}`;
    return await axios.get(url).then(res => res.data);
}

export default function Album(){
    const album = useLoaderData();
    const imgPath = `../images/album_${album.id}.jpg`;
    return (
        <>
            <img className="mainImage" src={imgPath}></img>

            <h1>{album.title}</h1>
        </>
    );
}