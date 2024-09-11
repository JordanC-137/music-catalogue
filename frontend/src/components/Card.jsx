export default function Card({value}){
    return (
        <div className = 'card-div'>
            <h3>{ value.title }</h3>
        </div>
    );
}