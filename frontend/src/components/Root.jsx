import { Outlet } from "react-router-dom";

export default function Root(){
    return (
        <>
            <div className="sidebar">
                <p>Sidebar placeholder</p>
            </div>
            <section className="main-component">
                <h1>Root component</h1>
                <Outlet />
            </section>
        </>
    );
}