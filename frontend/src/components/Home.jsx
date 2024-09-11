import { useState } from 'react';
import axios from 'axios';
import { useLoaderData } from 'react-router-dom';

import Card from './Card';

/*
async function getList(){
    const x = await axios.get('http://127.0.0.1:8000/collection/');
    return x.data;
}
*/
export async function loader(){
    const url = 'http://127.0.0.1:8000/collection/'
    return await axios.get(url).then(res => res.data);
}

export default function Home(){
    const values = useLoaderData();
    const cards = values.map((x) => <Card key = {x.id} value = {x}/>);
    return (
        <div className="flex-container">
            {cards}
        </div>
    );
}