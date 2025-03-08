import React, { useEffect, useState } from 'react';

const PlayerStats = ({ playerId }) => {
    const [playerData, setPlayerData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPlayerData = async () => {
            try {
                const response = await fetch(`/api/players/${playerId}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setPlayerData(data);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };

        fetchPlayerData();
    }, [playerId]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div>
            <h2>{playerData.name}</h2>
            <p>Matches: {playerData.matches}</p>
            <p>Runs: {playerData.runs}</p>
            <p>Wickets: {playerData.wickets}</p>
            <p>Average: {playerData.average}</p>
            <p>Strike Rate: {playerData.strikeRate}</p>
        </div>
    );
};

export default PlayerStats;