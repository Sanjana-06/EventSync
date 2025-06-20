import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Text } from 'react-native';

export default function App() {
  const [event, setEvent] = useState('');
  const [response, setResponse] = useState('');

  const handleInvite = async () => {
  try {
    const res = await fetch('http://192.168.0.8:5000/send-invitation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ event })
    });

    const data = await res.json();
    console.log("Server response:", data);

    if (res.ok) {
      setResponse(data.message || "Invitation sent");
    } else {
      setResponse("❌ Error: " + (data.error || "Unknown error"));
    }
  } catch (error) {
    console.error("Fetch error:", error);
    setResponse('❌ Failed to send invitation');
  }
};

  return (
    <View style={styles.container}>
      <Text style={styles.title}>EventSync - Host</Text>
      <TextInput
        placeholder="Enter event name"
        value={event}
        onChangeText={setEvent}
        style={styles.input}
      />
      <Button title="Send Invitation" onPress={handleInvite} />
      <Text>{response}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 20 },
  input: { borderWidth: 1, padding: 10, marginBottom: 20 },
  title: { fontSize: 20, marginBottom: 10, fontWeight: 'bold' }
});
