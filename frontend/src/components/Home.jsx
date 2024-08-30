import { useState } from 'react';
import axios from 'axios';

export default function Home(){
    const [albums, setAlbums] = useState([]);

    axios.get('http://127.0.0.1:8000/collection/')
    .then(res => {
        setAlbums(res.data);
    })
    .catch(err => console.log(err));

    const elems = albums.length === 0 ? albums.map(album => <li key={album.id}>{album.title}</li>) : <h1>Nothing</h1>;
    return (
        <>
            { elems }
        </>
    );
}